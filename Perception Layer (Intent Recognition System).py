def resolve_intent(query):
    clean_query = query.lower().strip()
    routing_logic = {"overheating": "thermal_diagnostic_v1", "slow": "io_performance_audit", "network": "connectivity_remediation"}
    for keyword, module in routing_logic.items():
        if keyword in clean_query:
            return execute_diagnostic(module)
    return escalate_to_human(clean_query)