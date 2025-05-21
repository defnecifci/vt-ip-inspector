def is_malicious_or_suspicious(analysis_stats):
    """
    last_analysis_stats kullanılarak IP'nin zararlı ya da şüpheli olup olmadığı belirlenir.
    """
    if not analysis_stats:
        return False

    malicious_count = analysis_stats.get("malicious", 0)
    suspicious_count = analysis_stats.get("suspicious", 0)

    return (malicious_count + suspicious_count) > 0
