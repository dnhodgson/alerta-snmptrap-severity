import logging
from alerta.exceptions import RateLimit
from alerta.plugins import PluginBase
import yaml

LOG = logging.getLogger('alerta.plugins.snmptrapseverity')


class SNMPTrapSeverity(PluginBase):

    def __init__(self):
        super(SNMPTrapSeverity, self).__init__(SNMPTrapSeverity)
        SNMPTRAP_SEVERITY_FILE = self.get_config('SNMPTRAP_SEVERITY_FILE',
                                                        default="/etc/alerta-snmptrapseverity.yml",
                                                        type=str)
        LOG.warning(SNMPTRAP_SEVERITY_FILE)
        self.severity_map = yaml.safe_load(open(SNMPTRAP_SEVERITY_FILE))

    def pre_receive(self, alert):
        if alert.attributes['trapvars']['_O'] in self.severity_map:
            try:
                LOG.info("Found {}".format(alert.attributes['trapvars']['_O']))
                alert.severity = self.severity_map[alert.attributes['trapvars']['_O']]['severity']
            except:
                pass
        return alert

    def post_receive(self, alert):
        return

    def status_change(self, alert, status, text):
        return
