# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

"""
L2 Domain tests scenarios
"""

from azure.cli.testsdk import ScenarioTest

from .config import CONFIG


def setup_scenario1(test):
    """Env setup_scenario1"""
    pass


def cleanup_scenario1(test):
    """Env cleanup_scenario1"""
    pass


def call_scenario1(test):
    """# Testcase: scenario1"""
    setup_scenario1(test)
    step_create(test, checks=[])
    step_show(test, checks=[])
    step_update(test, checks=[])
    step_list_resource_group(test, checks=[])
    step_list_subscription(test, checks=[])
    step_update_admin_state_Enable(test, checks=[])
    step_update_admin_state_Disable(test, checks=[])
    step_delete(test, checks=[])
    cleanup_scenario1(test)


def step_create(test, checks=None):
    """l2domain create operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain create --resource-group {rg} --resource-name {name} --location {location} --nf-id {nfId}"
        " --vlan-id {vlanId} --mtu {mtu} --extended-vlan {extendedVlan}",
        checks=checks,
    )


def step_show(test, checks=None):
    """l2domain show operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain show --resource-name {name} --resource-group {rg}"
    )


def step_update(test, checks=None):
    """l2domain update operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain update --resource-group {rg} --resource-name {name} --mtu {updatedMtu} --nni-id {nniId}",
        checks=checks,
    )


def step_list_resource_group(test, checks=None):
    """l2domain list by resource group operation"""
    if checks is None:
        checks = []
    test.cmd("az networkfabric l2domain list --resource-group {rg}")


def step_list_subscription(test, checks=None):
    """l2domain list by subscription operation"""
    if checks is None:
        checks = []
    test.cmd("az networkfabric l2domain list")


def step_update_admin_state_Enable(test, checks=None):
    """l2domain Update admin state operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain update-admin-state --resource-group {rg} --resource-name {name} --state {stateEnable}"
    )


def step_update_admin_state_Disable(test, checks=None):
    """l2domain Update admin state operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain update-admin-state --resource-group {rg} --resource-name {name} --state {stateDisable}"
    )


def step_delete(test, checks=None):
    """l2domain delete operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric l2domain delete --resource-name {name} --resource-group {rg}"
    )


class GA_L2DomainScenarioTest1(ScenarioTest):
    """L2 Domain Scenario test"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update(
            {
                "name": CONFIG.get("L2_ISOLATION_DOMAIN", "name"),
                "rg": CONFIG.get("L2_ISOLATION_DOMAIN", "resource_group"),
                "location": CONFIG.get("L2_ISOLATION_DOMAIN", "location"),
                "nfId": CONFIG.get("L2_ISOLATION_DOMAIN", "nf_id"),
                "mtu": CONFIG.get("L2_ISOLATION_DOMAIN", "mtu"),
                "vlanId": CONFIG.get("L2_ISOLATION_DOMAIN", "vlan_id"),
                "updatedMtu": CONFIG.get("L2_ISOLATION_DOMAIN", "updated_mtu"),
                "stateEnable": CONFIG.get("L2_ISOLATION_DOMAIN", "state_enable"),
                "stateDisable": CONFIG.get("L2_ISOLATION_DOMAIN", "state_disable"),
                "nniId": CONFIG.get("L2_ISOLATION_DOMAIN", "nni_id"),
                "extendedVlan": CONFIG.get("L2_ISOLATION_DOMAIN", "extended_vlan"),
            }
        )

    def test_GA_l2domain_scenario1(self):
        """test scenario for L2 Domain CRUD operations"""
        call_scenario1(self)
