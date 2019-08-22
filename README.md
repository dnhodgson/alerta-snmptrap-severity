# alerta-transform-oid
Alerta plugin to transform the severity of SNMP traps

Add the following to your alertad.conf file
    PLUGINS = ['snmptrapseverity']

Default map file is "/etc/alerta-snmptrapseverity.yml" but can be overwritten with SNMPTRAP_SEVERITY_FILE environment variable.

Example of severity map file
      "1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1":
        "severity": "informational"
      "NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatNotification":
        "severity": "informational"
