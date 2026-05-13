import logging
logging.basicConfig(level=logging.INFO)
def audit_pipeline_health(input_tensor, expected_features):
    if input_tensor.shape[1] != expected_features:
        logging.error("SKEW DETECTED")
        return False
    return True