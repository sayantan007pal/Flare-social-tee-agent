import os
import time
import logging
from threading import Thread

from x_account_manager import XAccountManager
from social_media_monitor import SocialMediaMonitor
from ai_processor import AIProcessor
from safety_filter import SafetyFilter
from attestation_manager import AttestationManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('flare_social_agent')

class FlareSocialAgent:
    def __init__(self):
        logger.info("Initializing Flare Social Agent...")
        
        # Initialize components
        self.x_manager = XAccountManager()
        self.monitor = SocialMediaMonitor()
        self.ai_processor = AIProcessor()
        self.safety_filter = SafetyFilter()
        self.attestation_manager = AttestationManager()
        
        # Internal state
        self.running = False
        self.attestation_valid = False
        
    def start(self):
        """Start the social media agent"""
        logger.info("Starting agent...")
        
        # First verify attestation
        self.verify_attestation()
        
        if not self.attestation_valid:
            logger.error("Attestation failed, cannot start agent")
            return False
            
        # Start monitoring thread
        self.running = True
        self.monitor_thread = Thread(target=self.run_monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        # Start attestation verification thread
        self.attestation_thread = Thread(target=self.run_attestation_loop)
        self.attestation_thread.daemon = True
        self.attestation_thread.start()
        
        logger.info("Agent started successfully")
        return True
        
    def verify_attestation(self):
        """Verify TEE attestation both locally and on-chain"""
        try:
            # Local verification
            local_verification = self.attestation_manager.verify_local()
            
            # On-chain verification
            onchain_verification = self.attestation_manager.verify_on_chain()
            
            self.attestation_valid = local_verification and onchain_verification
            
            logger.info(f"Attestation verification: {self.attestation_valid}")
            
            # If verification fails, trigger shutdown
            if not self.attestation_valid:
                logger.warning("Attestation verification failed, agent cannot operate")
        except Exception as e:
            logger.error(f"Attestation verification error: {str(e)}")
            self.attestation_valid = False
            
        return self.attestation_valid
            
    def run_monitor_loop(self):
        """Main loop for monitoring social media"""
        while self.running:
            try:
                # Set up callback for tweet processing
                self.monitor.monitor_mentions(self.process_tweet)
                
                # Sleep to avoid busy waiting
                time.sleep(1)
            except Exception as e:
                logger.error(f"Error in monitor loop: {str(e)}")
                time.sleep(5)  # Back off on error
                
    def run_attestation_loop(self):
        """Periodically verify attestation"""
        while self.running:
            try:
                # Re-verify attestation every hour
                time.sleep(3600)
                
                attestation_result = self.verify_attestation()
                
                # If attestation fails, initiate shutdown
                if not attestation_result:
                    logger.warning("Periodic attestation check failed, shutting down")
                    self.shutdown("Attestation failure")
            except Exception as e:
                logger.error(f"Error in attestation loop: {str(e)}")
                time.sleep(60)  # Back off on error
    
    def process_tweet(self, tweet):
        """Process an incoming tweet"""
        try:
            # Verify attestation is still valid
            if not self.attestation_valid:
                logger.warning("Cannot process tweet, attestation invalid")
                return
                
            logger.info(f"Processing tweet: {tweet.id}")
            
            # Classify the tweet
            classified_tweet = self.monitor.classify_tweet(tweet.text)
            
            # Skip if not relevant to Flare
            if classified_tweet["relevance_score"] < 0.6:
                logger.info(f"Tweet {tweet.id} not relevant to Flare, skipping")
                return
                
            # Process with AI
            ai_response = self.ai_processor.process_tweet(classified_tweet)
            
            # Apply safety filters
            is_safe, checks = self.safety_filter.check_response(ai_response)
            
            if not is_safe:
                logger.warning(f"Safety check failed for tweet {tweet.id}: {checks}")
                return
                
            # Post response
            if ai_response["confidence"] > 0.8:
                self.x_manager.post_tweet(
                    content=ai_response["proposed_response"],
                    in_reply_to_tweet_id=tweet.id
                )
                logger.info(f"Posted response to tweet {tweet.id}")
            else:
                logger.info(f"Low confidence ({ai_response['confidence']}) for tweet {tweet.id}, no response posted")
                
        except Exception as e:
            logger.error(f"Error processing tweet {tweet.id if 'tweet' in locals() else 'unknown'}: {str(e)}")
    
    def shutdown(self, reason="User requested"):
        """Gracefully shutdown the agent"""
        logger.info(f"Shutting down agent: {reason}")
        
        # Stop processing new tweets
        self.running = False
        
        # Notify smart contract of shutdown if attestation is valid
        if self.attestation_valid:
            try:
                self.attestation_manager.contract.functions.shutdownAgent(reason).transact({
                    'from': self.attestation_manager.account.address
                })
            except Exception as e:
                logger.error(f"Failed to notify contract of shutdown: {str(e)}")
        
        logger.info("Agent shutdown complete")

if __name__ == "__main__":
    agent = FlareSocialAgent()
    
    if agent.start():
        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            agent.shutdown("User terminated")
    else:
        logger.critical("Failed to start agent, exiting")