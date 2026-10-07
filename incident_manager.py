"""
Incident Response Playbook Templates

Structured incident response procedures for common incident types.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class IncidentSeverity(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class IncidentStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CONTAINED = "Contained"
    RESOLVED = "Resolved"
    CLOSED = "Closed"


@dataclass
class IncidentPlaybook:
    """Incident response playbook template"""
    
    incident_type: str
    severity: IncidentSeverity
    detection_indicators: List[str]
    immediate_actions: List[str]
    investigation_steps: List[str]
    containment_steps: List[str]
    communication_plan: dict
    recovery_steps: List[str]
    post_incident_review: List[str]


# Data Breach Playbook
DATA_BREACH_PLAYBOOK = IncidentPlaybook(
    incident_type="Data Breach",
    severity=IncidentSeverity.CRITICAL,
    detection_indicators=[
        "Unauthorized data access alerts",
        "Unusual database queries",
        "Large data exports",
        "Security tool alerts",
        "External notification of leaked data"
    ],
    immediate_actions=[
        "Activate incident response team",
        "Isolate affected systems",
        "Preserve evidence and logs",
        "Notify leadership",
        "Begin incident tracking"
    ],
    investigation_steps=[
        "Determine scope of breach",
        "Identify affected records",
        "Determine data types exposed",
        "Trace attacker actions",
        "Document findings"
    ],
    containment_steps=[
        "Reset passwords for affected accounts",
        "Block unauthorized access",
        "Patch vulnerable systems",
        "Revoke compromised credentials",
        "Update firewall rules"
    ],
    communication_plan={
        "internal": "Notify CEO, CIO, Legal within 1 hour",
        "external": "Kenya DPA notification within 72 hours",
        "customers": "Notify affected individuals (if required by DPA)"
    },
    recovery_steps=[
        "Restore systems from clean backups",
        "Verify system integrity",
        "Re-enable normal operations",
        "Monitor for follow-up attacks"
    ],
    post_incident_review=[
        "Root cause analysis",
        "Timeline reconstruction",
        "Control gaps identified",
        "Recommendations for prevention",
        "Policy updates"
    ]
)


# Malware Incident Playbook
MALWARE_PLAYBOOK = IncidentPlaybook(
    incident_type="Malware Infection",
    severity=IncidentSeverity.HIGH,
    detection_indicators=[
        "Antivirus alerts",
        "Unusual process execution",
        "Network traffic anomalies",
        "System performance degradation",
        "User reports of suspicious activity"
    ],
    immediate_actions=[
        "Isolate infected systems from network",
        "Stop suspicious processes",
        "Capture system images",
        "Alert users on affected devices",
        "Activate incident response"
    ],
    investigation_steps=[
        "Identify malware type/family",
        "Determine infection vector",
        "Check for lateral movement",
        "Review system logs",
        "Identify affected systems"
    ],
    containment_steps=[
        "Disable affected user accounts",
        "Block malware signatures",
        "Scan all systems",
        "Update antivirus definitions",
        "Block C&C communications"
    ],
    communication_plan={
        "internal": "Notify IT security team immediately",
        "external": "Alert antivirus vendors if new threat"
    },
    recovery_steps=[
        "Clean or rebuild affected systems",
        "Restore from clean backups",
        "Verify malware removal",
        "Monitor for reinfection",
        "Restore normal operations"
    ],
    post_incident_review=[
        "Malware analysis report",
        "Infection timeline",
        "Vulnerability assessment",
        "User education on vectors",
        "Email filter improvements"
    ]
)


# DDoS Attack Playbook
DDOS_PLAYBOOK = IncidentPlaybook(
    incident_type="DDoS Attack",
    severity=IncidentSeverity.HIGH,
    detection_indicators=[
        "Network traffic spike",
        "Service unavailability",
        "Load balancer alerts",
        "High bandwidth consumption",
        "Slow response times"
    ],
    immediate_actions=[
        "Verify DDoS vs legitimate traffic",
        "Notify DDoS mitigation service",
        "Increase network capacity",
        "Activate backup systems",
        "Document attack details"
    ],
    investigation_steps=[
        "Identify attack vectors",
        "Analyze traffic patterns",
        "Determine attack source",
        "Estimate attack duration",
        "Track attack evolution"
    ],
    containment_steps=[
        "Activate DDoS mitigation",
        "Filter malicious traffic",
        "Rate limiting",
        "IP blacklisting",
        "DNS failover if needed"
    ],
    communication_plan={
        "internal": "Notify leadership and ops team",
        "external": "Customer communications if service down"
    },
    recovery_steps=[
        "Monitor traffic patterns",
        "Gradually return to normal",
        "Verify service health",
        "Remove temporary blocks",
        "Restore normal operations"
    ],
    post_incident_review=[
        "Attack analysis",
        "Mitigation effectiveness",
        "DDoS prevention improvements",
        "ISP coordination review",
        "Service restoration procedures"
    ]
)


class IncidentManager:
    """Manage incident response"""
    
    def __init__(self):
        self.incidents = []
    
    def create_incident(self, incident_type: str, severity: IncidentSeverity):
        """Create new incident from playbook"""
        playbooks = {
            "Data Breach": DATA_BREACH_PLAYBOOK,
            "Malware": MALWARE_PLAYBOOK,
            "DDoS": DDOS_PLAYBOOK
        }
        
        if incident_type in playbooks:
            return playbooks[incident_type]
        return None
    
    def export_playbook(self, playbook: IncidentPlaybook, filename: str):
        """Export playbook to text file"""
        with open(filename, 'w') as f:
            f.write(f"Incident Response Playbook: {playbook.incident_type}\n")
            f.write(f"Severity: {playbook.severity.value}\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            
            f.write("Detection Indicators:\n")
            for indicator in playbook.detection_indicators:
                f.write(f"  - {indicator}\n")
            
            f.write("\nImmediate Actions:\n")
            for action in playbook.immediate_actions:
                f.write(f"  - {action}\n")
            
            f.write("\nCommunication Plan:\n")
            for party, message in playbook.communication_plan.items():
                f.write(f"  - {party}: {message}\n")


if __name__ == "__main__":
    manager = IncidentManager()
    
    # Export all playbooks
    playbooks = [DATA_BREACH_PLAYBOOK, MALWARE_PLAYBOOK, DDOS_PLAYBOOK]
    
    for playbook in playbooks:
        filename = f"playbook_{playbook.incident_type.lower().replace(' ', '_')}.txt"
        manager.export_playbook(playbook, filename)
        print(f"Exported: {filename}")
