# Alerta SNMP Trap Severity Plugin
Alerta plugin to transform the severity of SNMP traps

Add the following to your alertad.conf file
    PLUGINS = ['snmptrapseverity']

Default map file is "/etc/alerta-snmptrapseverity.yml" but can be overwritten with SNMPTRAP_SEVERITY_FILE environment variable.

Example of severity map file

       "1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.4.1.8072.2.3.2.1":
         "severity": "informational"
       "NET-SNMP-EXAMPLES-MIB::netSnmpExampleHeartbeatNotification":
         "severity": "informational"

If you are using docker for Alerta you can build a layer on top of the image and install the plugin with the following docker file
        FROM alerta/alerta-web:latest
        WORKDIR /venv
        RUN git clone https://github.com/dnhodgson/alerta-snmptrap-severity.git
        RUN bin/python3 alerta-snmptrap-severity/setup.py install

You can link in your severity file when you run the container.
        docker run ... -v alerta-snmptrapseverity.yml:/etc/alerta-snmptrapseverity.yml ...
