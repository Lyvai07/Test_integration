# tests/test_ad_dns_unit.py
from unittest.mock import patch, MagicMock
import importlib

# On importe le module après l'avoir renommé (Diag_AD_DNS.py)
Diag = importlib.import_module("src.Diag_AD_DNS")

@patch("src.Diag_AD_DNS.dns.resolver.Resolver")
def test_dns_ok(mock_resolver_cls):
    # Simule une réponse DNS "A"
    mock_resolver = MagicMock()
    mock_resolver.resolve.return_value = [MagicMock(to_text=lambda: "10.0.0.1")]
    mock_resolver_cls.return_value = mock_resolver

    ok, msg = Diag.check_dns("10.0.0.1", "corp.local")
    assert ok is True
    assert "Résolu" in msg

@patch("src.Diag_AD_DNS.Connection")
@patch("src.Diag_AD_DNS.Server")
def test_ldap_ok(mock_server_cls, mock_conn_cls):
    # Simule un bind LDAP réussi
    mock_conn = MagicMock()
    mock_conn_cls.return_value = mock_conn

    ok, msg = Diag.check_ad_ldap("10.0.0.1", "CORP\\user", "pass")
    assert ok is True
    assert "Authentification réussie" in msg