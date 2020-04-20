# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['eventgrid'] = """
type: group
short-summary: Manage Azure Event Grid topics, domains, domain topics, system topics partner topics, event subscriptions, system topic event subscriptions and partner topic event subscriptions.
"""

helps['eventgrid domain'] = """
type: group
short-summary: Manage event domains.
"""

helps['eventgrid domain create'] = """
type: command
short-summary: Create a domain.
parameters:
  - name: --inbound-ip-rules
    short-summary: List of inbound IP rules.
    long-summary: |
        List of inbound IP rules specifying IP Address in CIDR notation e.g., 10.0.0.0/8 along with corresponding Action to perform based on the match or no match of the IpMask. Possible values include - Allow.
examples:
  - name: Create a new domain.
    text: az eventgrid domain create -g rg1 --name domain1 -l westus2
  - name: Create a new domain with custom input mappings.
    text: az eventgrid domain create -g rg1 --name domain1 -l westus2 --input-schema customeventschema --input-mapping-fields topic=mytopicField eventType=myEventTypeField --input-mapping-default-values subject=DefaultSubject dataVersion=1.0
  - name: Create a new domain that accepts events published in CloudEvents V1.0 schema and maps a property mytopicfield to the topic name.
    text: az eventgrid domain create -g rg1 --name domain1 -l westus2 --input-schema cloudeventschemav1_0 --input-mapping-fields topic=mytopicfield
  - name: Create a new domain which allows specific inbound ip rules.
    text: az eventgrid domain create -g rg1 --name domain1 -l westus2 --public-network-access enabled --inbound-ip-rules 10.0.0.0/8 Allow --inbound-ip-rules 10.2.0.0/8 Allow --sku basic

"""

helps['eventgrid domain delete'] = """
type: command
short-summary: Delete a domain.
examples:
  - name: Delete a domain.
    text: az eventgrid domain delete -g rg1 --name domain1
"""

helps['eventgrid domain private-endpoint-connection'] = """
type: group
short-summary: Manage private endpoint connection resources of a domain.
"""

helps['eventgrid domain private-endpoint-connection delete'] = """
type: command
short-summary: Delete a private endpoint connection for a domain.
examples:
  - name: Delete private endpoint connection for a specific domain.
    text: az eventgrid domain private-endpoint-connection delete -g rg1 --domain-name domain1 -n connectionName1
"""

helps['eventgrid domain private-endpoint-connection show'] = """
type: command
short-summary: Display the properties of a private endpoint connection for a domain.
examples:
  - name: Show a private endpoint connection for a domain.
    text: az eventgrid domain private-endpoint-connection show -g rg1 --domain-name domain1 -n connectionName1
"""

helps['eventgrid domain private-endpoint-connection list'] = """
type: command
short-summary: List the properties of all the private endpoint connections for a domain.
examples:
  - name: List a private endpoint connection for a domain.
    text: az eventgrid domain private-endpoint-connection list -g rg1 -n domain1
"""

helps['eventgrid domain private-endpoint-connection approve'] = """
type: command
short-summary: Approve a private endpoint connection request for a domain.
examples:
  - name: Approve a private endpoint connection for a domain.
    text: az eventgrid domain private-endpoint-connection approve -g rg1 --domain-name domain1 -n domain1-PrivateEndpoint.6d90cf76-a022-452c-9994-6dac62a50c99 --description "Sample approval description"
"""

helps['eventgrid domain private-endpoint-connection reject'] = """
type: command
short-summary: Reject a private endpoint connection request for a domain.
examples:
  - name: Reject a private endpoint connection for a domain.
    text: az eventgrid domain private-endpoint-connection reject -g rg1 --domain-name domain1 -n domain1-PrivateEndpoint.6d90cf76-a022-452c-9994-6dac62a50c99 --description "Sample rejection description"
"""

helps['eventgrid domain private-link-resource'] = """
type: group
short-summary: Manage private link resource of a domain.
"""

helps['eventgrid domain private-link-resource show'] = """
type: command
short-summary: Display the properties of a private link resource for a domain.
examples:
  - name: Show a private endpoint connection for a domain.
    text: az eventgrid domain private-link-resource show -g rg1 --domain-name domain1 -n domain
"""

helps['eventgrid domain private-link-resource list'] = """
type: command
short-summary: List the properties of all the private link resources for a domain.
examples:
  - name: Show a private endpoint connection for a domain.
    text: az eventgrid domain private-link-resource list -g rg1 --domain-name domain1
"""


helps['eventgrid domain key'] = """
type: group
short-summary: Manage shared access keys of a domain.
"""

helps['eventgrid domain key list'] = """
type: command
short-summary: List shared access keys of a domain.
examples:
  - name: List shared access keys of a domain. (autogenerated)
    text: az eventgrid domain key list --name MyDomain --resource-group MyResourceGroup
    crafted: true
"""

helps['eventgrid domain key regenerate'] = """
type: command
short-summary: Regenerate a shared access key of a domain.
"""

helps['eventgrid domain list'] = """
type: command
short-summary: List available domains.
examples:
  - name: List all domains in the current Azure subscription.
    text: az eventgrid domain list
  - name: List all domains in a resource group.
    text: az eventgrid domain list -g rg1
  - name: List all domains in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid domain list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all domains in a resource group except the domain with name "name1"
    text: az eventgrid domain list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid domain show'] = """
type: command
short-summary: Get the details of a domain.
examples:
  - name: Show the details of a domain.
    text: az eventgrid domain show -g rg1 -n domain1
  - name: Show the details of a domain based on resource ID.
    text: az eventgrid domain show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
"""

helps['eventgrid domain topic'] = """
type: group
short-summary: Manage event domain topics.
"""

helps['eventgrid domain topic create'] = """
type: command
short-summary: Create a domain topic under a domain.
examples:
  - name: Create a new domain topic under domain.
    text: az eventgrid domain topic create -g rg1 --domain-name domain1 --name domaintopic1
"""

helps['eventgrid domain topic delete'] = """
type: command
short-summary: Delete a domain topic under a domain.
examples:
  - name: Delete a domain topic.
    text: az eventgrid domain topic delete -g rg1 --domain-name domain1 --name domaintopic1
"""

helps['eventgrid domain topic list'] = """
type: command
short-summary: List available topics in a domain.
examples:
  - name: List all topics in a domain.
    text: az eventgrid domain topic list -g rg1 --domain-name domain1
  - name: List all domain topics in a domain whose name contains the pattern "XYZ"
    text: az eventgrid domain topic list -g rg1 --domain-name domain1 --odata-query "Contains(name, 'XYZ')"
  - name: List all domain topics in a domain except the domain topic with name "name1"
    text: az eventgrid domain topic list -g rg1 --domain-name domain1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid domain topic show'] = """
type: command
short-summary: Get the details of a domain topic.
examples:
  - name: Show the details of a domain topic.
    text: az eventgrid domain topic show -g rg1 --domain-name domain1 --name topic1
"""

helps['eventgrid domain update'] = """
type: command
short-summary: Update a domain.
parameters:
  - name: --inbound-ip-rules
    short-summary: List of inbound IP rules.
    long-summary: |
        List of inbound IP rules specifying IP Address in CIDR notation e.g., 10.0.0.0/8 along with corresponding Action to perform based on the match or no match of the IpMask. Possible values include - Allow.
examples:
  - name: Update the properties of an existing domain.
    text: az eventgrid domain update -g rg1 --name domain1 --sku Basic --identity noidentity --public-network-access enabled --inbound-ip-rules 10.0.0.0/8 Allow --inbound-ip-rules 10.2.0.0/8 Allow --tags Dept=IT --sku basic
"""

helps['eventgrid partner'] = """
type: group
short-summary: Manage partner resources.
"""

helps['eventgrid partner registration'] = """
type: group
short-summary: Manage partner registrations.
"""

helps['eventgrid partner registration create'] = """
type: command
short-summary: Create a new partner registration.
examples:
  - name: Create a new partner registration with basic information.
    text: az eventgrid partner registration create -g rg1 --name partnerRegistrationName1 --partner-name Contoso --resource-type-name Accounts --authorized-subscription-ids 533ad9de-25db-46e2-b94a-d00c37cf022b 05aa2228-7d34-4635-922d-2b582c422445
  - name: Create a new partner registration with partner information.
    text: az eventgrid partner registration create -g rg1 --name partnerRegistrationName1 --partner-name Contoso --resource-type-name Accounts --authorized-subscription-ids 533ad9de-25db-46e2-b94a-d00c37cf022b 05aa2228-7d34-4635-922d-2b582c422445 --description ExampleDescription --display-name ExampleDisplayName1 --logo-uri https://www.example.com/logo.png --setup-uri https://www.example.com
"""

helps['eventgrid partner registration list'] = """
type: command
short-summary: List all partner registrations in specific resource group or all under the specified azure subscription.
examples:
  - name: List all partner registrations in the current Azure subscription.
    text: az eventgrid partner registration list
  - name: List all partner registrations in a resource group.
    text: az eventgrid partner registration list -g rg1
  - name: List all partner registrations in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid partner registration list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all partner registrations in a resource group except the partner registration with name "name1"
    text: az eventgrid partner registration list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid partner namespace'] = """
type: group
short-summary: Manage partner namespaces.
"""

helps['eventgrid partner namespace create'] = """
type: command
short-summary: Create a partner namespace.
examples:
  - name: Create a new partner namespace.
    text: az eventgrid partner namespace create -g rg1 --name namespaceName1 -l westus2 --partner-registration-id 795c9f2f-6d2d-42ff-a570-42fd3043192c
"""

helps['eventgrid partner namespace list'] = """
type: command
short-summary: List available partner namespaces.
examples:
  - name: List all partner namespaces in the current Azure subscription.
    text: az eventgrid partner namespace list
  - name: List all partner namespaces in a resource group.
    text: az eventgrid partner namespace list -g rg1
  - name: List all partner namespaces in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid partner namespace list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all partner namespaces in a resource group except the partner namespace with name "name1"
    text: az eventgrid partner namespace list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid partner namespace delete'] = """
type: command
short-summary: Delete a partner namespace.
examples:
  - name: Delete a specific partner namespace.
    text: az eventgrid partner namespace delete -g rg1 --name partnernamespace1
"""

helps['eventgrid partner namespace show'] = """
type: command
short-summary: Get the details of a partner namespace.
examples:
  - name: Show the details of a partner namespace.
    text: az eventgrid partner namespace show -g rg1 -n partnernamespace1
  - name: Show the details of a partner namespace based on resource ID.
    text: az eventgrid partner namespace show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/partnenamespaces/partnernamespace1
"""

helps['eventgrid partner namespace key'] = """
type: group
short-summary: Manage shared access keys of a partner namespace.
"""

helps['eventgrid partner namespace key list'] = """
type: command
short-summary: List shared access keys of a partner namespace.
examples:
  - name: List shared access keys of a partner namespace (autogenerated)
    text: az eventgrid partner namespace key list --partner-namespace-name MyNamespace --resource-group MyResourceGroup
    crafted: true
"""

helps['eventgrid partner namespace key regenerate'] = """
type: command
short-summary: Regenerate a shared access key of a partner namespace.
"""

helps['eventgrid partner namespace event-channel'] = """
type: group
short-summary: Manage partner event channels.
"""

helps['eventgrid partner namespace event-channel create'] = """
type: command
short-summary: Create an event channel under a partner namespace.
examples:
  - name: Create a specific event-channel.
    text: az eventgrid partner namespace event-channel create -g rg1 --partner-namespace-name partnernamespace1 -n eventChannelName1 --source SourceExample1 --destination-subscription-id 61f7c265-374d-499e-866d-5f4cc302b888 --destination-resource-group rg2 --desination-topic-name topicName1
"""

helps['eventgrid partner namespace event-channel list'] = """
type: command
short-summary: List available partner event-channels.
examples:
  - name: List all event-channels in a specific partner namespace.
    text: az eventgrid partner namespace event-channel list -g rg1 --partner-namespace-name partnernamespace1
  - name: List all event channel under a partner namespace whose name contains the pattern "XYZ"
    text: az eventgrid partner namespace event-channel list -g rg1 --partner-namespace-name partnernamespace1  --odata-query "Contains(name, 'XYZ')"
"""

helps['eventgrid partner namespace event-channel delete'] = """
type: command
short-summary: Delete a partner namespace.
examples:
  - name: Delete a specific partner namespace.
    text: az eventgrid partner namespace event-channel delete -g rg1 --partner-namespace-name partnernamespace1 -n eventChannelName1
"""

helps['eventgrid partner namespace event-channel show'] = """
type: command
short-summary: Get the details of an event channel under a partner namespace.
examples:
  - name: Show the details of an event channel.
    text: az eventgrid partner namespace event-channel show -g rg1 --partner-namespace-name partnernamespace1 -n eventChannelName1
  - name: Show the details of an event-channel based on resource ID.
    text: az eventgrid partner namespace event-channel show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/partnenamespaces/partnernamespace1/eventChannels/eventChannelName1
"""


helps['eventgrid partner topic'] = """
type: group
short-summary: Manage partner topics.
"""

helps['eventgrid system-topic'] = """
type: group
short-summary: Manage system topics.
"""

helps['eventgrid system-topic create'] = """
type: command
short-summary: Create a system topic.
examples:
  - name: Create a new system topic for storage account source.
    text: az eventgrid system-topic create -g rg1 --name systemtopic1 --location westus2 --topic-type microsoft.storage.storageaccounts --source /subscriptions/1b3b4501-23b9-4790-c31b-ddbd88d72123/resourceGroups/rg2/providers/Microsoft.Storage/storageAccounts/stgaccountname

"""

helps['eventgrid system-topic delete'] = """
type: command
short-summary: Delete a system topic.
examples:
  - name: Delete a specific system topic.
    text: az eventgrid system-topic delete -g rg1 --name systemtopic1
"""

helps['eventgrid system-topic list'] = """
type: command
short-summary: List available system topics.
examples:
  - name: List all system topics in the current Azure subscription.
    text: az eventgrid system-topic list
  - name: List all system topics in a resource group.
    text: az eventgrid system-topic list -g rg1
  - name: List all system topics in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid system-topic list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all system topics in a resource group except the system topic with name "name1"
    text: az eventgrid system-topic list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid system-topic show'] = """
type: command
short-summary: Get the details of a system topic.
examples:
  - name: Show the details of a system topic.
    text: az eventgrid system-topic show -g rg1 -n systemtopic1
  - name: Show the details of a system topic based on resource ID.
    text: az eventgrid system-topic show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/systemtopics/systemtopic1
"""

helps['eventgrid system-topic update'] = """
type: command
short-summary: Update a system topic.
examples:
  - name: Update the properties of an existing system topic.
    text: az eventgrid system-topic update -g rg1 --name systemtopic1 --tags Dept=IT
"""

helps['eventgrid partner topic list'] = """
type: command
short-summary: List available partner topics.
examples:
  - name: List all partner topics in the current Azure subscription.
    text: az eventgrid partner topic list
  - name: List all partner topics in a resource group.
    text: az eventgrid partner topic list -g rg1
  - name: List all partner topics in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid partner topic list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all partner topics in a resource group except the partner topic with name "name1"
    text: az eventgrid partner topic list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid partner topic delete'] = """
type: command
short-summary: Delete a partner topic.
examples:
  - name: Delete a specific partner topic.
    text: az eventgrid partner topic delete -g rg1 --name partnertopic1
"""

helps['eventgrid partner topic show'] = """
type: command
short-summary: Get the details of a partner topic.
examples:
  - name: Show the details of a partner topic.
    text: az eventgrid partner topic show -g rg1 -n partnertopic1
  - name: Show the details of a partner topic based on resource ID.
    text: az eventgrid partner topic show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/partnetopics/topic1
"""

helps['eventgrid partner topic activate'] = """
type: command
short-summary: Activate a partner topic.
examples:
  - name: Activate a specific partner topic.
    text: az eventgrid partner topic activate -g rg1 -n partnertopic1
"""

helps['eventgrid partner topic deactivate'] = """
type: command
short-summary: Deactivate a partner topic.
examples:
  - name: Deactivate a specific partner topic.
    text: az eventgrid partner topic deactivate -g rg1 -n partnertopic1
"""

helps['eventgrid system-topic event-subscription'] = """
type: group
short-summary: Manage event subscriptions of system topic.
"""

helps['eventgrid system-topic event-subscription create'] = """
type: command
short-summary: Create a new event subscription for a system topic
parameters:
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
  - name: --deadletter-endpoint
    short-summary: The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    long-summary: |
        Example: --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/containerName
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
examples:
  - name: Create a new event subscription for an Event Grid system topic, using default filters.
    text: |
        az eventgrid system-topic event-subscription create --name es1 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for an Event Grid system topic, with a filter specifying a subject prefix.
    text: |
        az eventgrid system-topic event-subscription create --name es4 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-begins-with mysubject_prefix
  - name: Create a new event subscription for an Event Grid system topic, using default filters, and CloudEvent V 1.0 as the delivery schema.
    text: |
      az eventgrid system-topic event-subscription create -n es2 \\
          -g rg1 --system-topic-name systemtopic1 \\
          --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
          --event-delivery-schema cloudeventschemav1_0
  - name: Create a new event subscription for an Event Grid system topic, with a deadletter destination and custom retry policy of maximum 10 delivery attempts and an Event TTL of 2 hours (whichever happens earlier) and expiration date.
    text: |
        az eventgrid system-topic event-subscription create --name es2 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 \\
            --max-delivery-attempts 10 --event-ttl 120 --expiration-date "2022-10-31"
  - name: Create a new event subscription for an Event Grid system topic, using Azure Active Directory enabled Webhook as a destination .
    text: |
        az eventgrid system-topic event-subscription create --name es1 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --azure_active_directory_tenant_id azureactivedirectorytenantid
            --azure_active_directory_application_id_or_uri azureactivedirectoryapplicationidoruri
  - name: Create a new event subscription for an Event Grid system topic, using Azure Function as destination.
    text: |
        az eventgrid system-topic event-subscription create -n es1 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Web/sites/{functionappname}/functions/{functionname} --endpoint-type azurefunction

"""

helps['eventgrid system-topic event-subscription delete'] = """
type: command
short-summary: Delete an event subscription of a system topic
examples:
  - name: Delete an event subscription for an Event Grid system topic.
    text: |
        az eventgrid system-topic event-subscription delete --name es1 \\
            -g rg1 --system-topic-name systemtopic1 \\
"""

helps['eventgrid system-topic event-subscription list'] = """
type: command
short-summary: List event subscriptions of a specific system topic.
examples:
  - name: List all event subscriptions created for an Event Grid system topic.
    text: |
        az eventgrid system-topic event-subscription list -g rg1 --system-topic-name systemtopic1
"""

helps['eventgrid system-topic event-subscription show'] = """
type: command
short-summary: Get the details of an event subscription of a system topic.
examples:
  - name: Show the details of an event subscription for an Event Grid system topic.
    text: |
        az eventgrid system-topic event-subscription show --name es1 \\
             -g rg1 --system-topic-name systemtopic1
"""

helps['eventgrid system-topic event-subscription update'] = """
type: command
short-summary: Update an event subscription of a system topic.
parameters:
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
examples:
  - name: Update an event subscription for an Event Grid system topic to specify a new endpoint.
    text: |
        az eventgrid system-topic event-subscription update --name es1 \\
            -g rg1 --system-topic-name systemtopic1 --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for an Event Grid system topic to specify a new subject-ends-with filter.
    text: |
        az eventgrid system-topic event-subscription update --name es2 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --subject-ends-with .jpg
  - name: Update an event subscription for an Event Grid system topic to specify a new endpoint and a new subject-ends-with filter a new list of included event types.
    text: |
        az eventgrid system-topic event-subscription update --name es3 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --subject-ends-with .png \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
  - name: Update an event subscription for an Azure Event Grid system topic, to include a deadletter destination.
    text: |
        az eventgrid system-topic event-subscription update --name es2 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/blobcontainer1
  - name: Update an event subscription for an Azure Event Grid system topic, using advanced filters.
    text: |
        az eventgrid system-topic event-subscription update --name es3 \\
            -g rg1 --system-topic-name systemtopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --advanced-filter data.blobType StringIn BlockBlob
            --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net

"""

helps['eventgrid partner topic event-subscription'] = """
type: group
short-summary: Manage event subscriptions of partner topic.
"""

helps['eventgrid partner topic event-subscription create'] = """
type: command
short-summary: Create a new event subscription for a partner topic
parameters:
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
  - name: --deadletter-endpoint
    short-summary: The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    long-summary: |
        Example: --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/containerName
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
examples:
  - name: Create a new event subscription for an Event Grid partner topic, using default filters.
    text: |
        az eventgrid partner topic event-subscription create --name es1 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for an Event Grid partner topic, with a filter specifying a subject prefix.
    text: |
        az eventgrid partner topic event-subscription create --name es4 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-begins-with mysubject_prefix
  - name: Create a new event subscription for an Event Grid partner topic, using default filters, and CloudEvent V 1.0 as the delivery schema.
    text: |
      az eventgrid partner topic event-subscription create -n es2 \\
          -g rg1 --partner-topic-name partnertopic1 \\
          --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
          --event-delivery-schema cloudeventschemav1_0
  - name: Create a new event subscription for an Event Grid partnertopic, with a deadletter destination and custom retry policy of maximum 10 delivery attempts and an Event TTL of 2 hours (whichever happens earlier) and expiration date.
    text: |
        az eventgrid partner topic event-subscription create --name es2 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 \\
            --max-delivery-attempts 10 --event-ttl 120 --expiration-date "2022-10-31"
  - name: Create a new event subscription for an Event Grid partner topic, using Azure Active Directory enabled Webhook as a destination .
    text: |
        az eventgrid partner topic event-subscription create --name es1 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --azure_active_directory_tenant_id azureactivedirectorytenantid
            --azure_active_directory_application_id_or_uri azureactivedirectoryapplicationidoruri
  - name: Create a new event subscription for an Event Grid partner topic, using Azure Function as destination.
    text: |
        az eventgrid partner topic event-subscription create -n es1 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Web/sites/{functionappname}/functions/{functionname} --endpoint-type azurefunction

"""

helps['eventgrid partner topic event-subscription delete'] = """
type: command
short-summary: Delete an event subscription of a partner topic
examples:
  - name: Delete an event subscription for an Event Grid partner topic.
    text: |
        az eventgrid partner topic event-subscription delete --name es1 \\
            -g rg1 --partner-topic-name partnertopic1 \\
"""

helps['eventgrid partner topic event-subscription list'] = """
type: command
short-summary: List event subscriptions of a specific partner topic.
examples:
  - name: List all event subscriptions created for an Event Grid partner topic.
    text: |
        az eventgrid partner topic event-subscription list -g rg1 --partner-topic-name partnertopic1
"""

helps['eventgrid partner topic event-subscription show'] = """
type: command
short-summary: Get the details of an event subscription of a partner topic.
examples:
  - name: Show the details of an event subscription for an Event Grid partner topic.
    text: |
        az eventgrid partner topic event-subscription show --name es1 \\
             -g rg1 --partner-topic-name partnertopic1
"""

helps['eventgrid partner topic event-subscription update'] = """
type: command
short-summary: Update an event subscription of a partner topic.
parameters:
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
examples:
  - name: Update an event subscription for an Event Grid partner topic to specify a new endpoint.
    text: |
        az eventgrid partner topic event-subscription update --name es1 \\
            -g rg1 --partner-topic-name partnertopic1 --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for an Event Grid partner topic to specify a new subject-ends-with filter.
    text: |
        az eventgrid partner topic event-subscription update --name es2 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --subject-ends-with .jpg
  - name: Update an event subscription for an Event Grid partner topic to specify a new endpoint and a new subject-ends-with filter a new list of included event types.
    text: |
        az eventgrid partner topic event-subscription update --name es3 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --subject-ends-with .png \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
  - name: Update an event subscription for an Azure Event Grid partner topic, to include a deadletter destination.
    text: |
        az eventgrid partner topic event-subscription update --name es2 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/blobcontainer1
  - name: Update an event subscription for an Azure Event Grid partner topic, using advanced filters.
    text: |
        az eventgrid partner topic event-subscription update --name es3 \\
            -g rg1 --partner-topic-name partnertopic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --advanced-filter data.blobType StringIn BlockBlob
            --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net

"""

helps['eventgrid event-subscription'] = """
type: group
short-summary: Manage event subscriptions.
long-summary: Manage event subscriptions for an Event Grid topic, domain, domain topic, Azure subscription, resource group or for any other Azure resource that supports event notifications.
"""

helps['eventgrid event-subscription create'] = """
type: command
short-summary: Create a new event subscription.
parameters:
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource to which the event subscription needs to be created.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
  - name: --deadletter-endpoint
    short-summary: The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    long-summary: |
        Example: --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/containerName
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
  - name: --delivery-identity-endpoint-type
    short-summary: The type of the destination endpoint with resource identity.
examples:
  - name: Create a new event subscription for an Event Grid topic, using default filters.
    text: |
        az eventgrid event-subscription create --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for an Azure subscription subscription, using default filters.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a resource group, using default filters.
    text: |
        az eventgrid event-subscription create --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a storage account, using default filters.
    text: |
        az eventgrid event-subscription create --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1"  \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription for a storage account, using advanced filters.
    text: |
        az eventgrid event-subscription create  --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --advanced-filter data.blobType StringIn BlockBlob
            --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net
  - name: Create a new event subscription for an Azure subscription, with a filter specifying a subject prefix.
    text: |
        az eventgrid event-subscription create --name es4 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-begins-with mysubject_prefix
  - name: Create a new event subscription for a resource group, with a filter specifying a subject suffix.
    text: |
        az eventgrid event-subscription create --name es5 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --subject-ends-with mysubject_suffix
  - name: Create a new event subscription for an Azure subscription, using default filters, and an EventHub as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type eventhub \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.EventHub/namespaces/n1/eventhubs/EH1
  - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure Storage queue as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type storagequeue \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/queueservices/default/queues/q1
  - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure ServiceBusQueue as a destination.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --endpoint-type servicebusqueue \\
            --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.ServiceBus/namespaces/ns1/queues/queue1
  - name: Create a new event subscription for an Event Grid domain, using default filters, and CloudEvent V 1.0 as the delivery schema.
    text: |
      az eventgrid event-subscription create --name es2 \\
          --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 \\
          --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
          --event-delivery-schema cloudeventschemav1_0
  - name: Create a new event subscription for a storage account, with a deadletter destination and custom retry policy of maximum 10 delivery attempts and an Event TTL of 2 hours (whichever happens earlier).
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 \\
            --max-delivery-attempts 10 --event-ttl 120
  - name: Create a new event subscription for a domain topic.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/t1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Create a new event subscription (for a storage account) with an expiration date.
    text: |
        az eventgrid event-subscription create --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/sa1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --expiration-date "2018-10-31"
  - name: Create a new event subscription for an Event Grid topic, using Azure Active Directory enabled Webhook as a destination .
    text: |
        az eventgrid event-subscription create --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --azure_active_directory_tenant_id azureactivedirectorytenantid
            --azure_active_directory_application_id_or_uri azureactivedirectoryapplicationidoruri
  - name: Create a new event subscription for an Event Grid topic, using Azure Function as destination.
    text: |
        az eventgrid event-subscription create --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Web/sites/{functionappname}/functions/{functionname} --endpoint-type azurefunction

  - name: Create a new event subscription for an Event Grid topic, using Eventhub with systemassigned MSI identity as destination and with deadletter with MSI identity
    text: |
        az eventgrid event-subscription create --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --delivery-identity-endpoint-type eventhub --delivery-identity systemassigned --delivery-identity-endpoint /subscriptions/{SubId2|}/resourceGroups/{RG2}/providers/Microsoft.eventhub/namespaces/{EventHubNamespace}/eventhubs/{EventhubName} \\
            --deadletter-identity-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 --deadletter-identity systemassigned -n {EventSubscriptionName}

"""

helps['eventgrid event-subscription delete'] = """
type: command
short-summary: Delete an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be deleted.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: Delete an event subscription for an Event Grid topic.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
  - name: Delete an event subscription for an Event Grid domain topic.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/topic1
  - name: Delete an event subscription for an Event Grid domain.
    text: |
        az eventgrid event-subscription delete --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
  - name: Delete an event subscription for an Azure subscription.
    text: |
        az eventgrid event-subscription delete --name es2 \\
            --source-resource-id /subscriptions/{SubID}
  - name: Delete an event subscription for a resource group.
    text: |
        az eventgrid event-subscription delete --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
  - name: Delete an event subscription for a storage account.
    text: |
        az eventgrid event-subscription delete --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob
"""

helps['eventgrid event-subscription list'] = """
type: command
short-summary: List event subscriptions.
long-summary: |
    Event Grid supports both regional and global event subscriptions: Event subscriptions on regional resources (such as Storage accounts or Event Grid topics) are regional, while event subscriptions on global resources (such as an Azure subscription or resource group) are global.
    Hence, you can list event subscriptions in a few different ways:
    1. To list by the resource ID of the resource whose event subscriptions you want to list, specify the --source-resource-id parameter. No other parameters must be specified.
    2. To list by a topic-type (e.g. storage accounts), specify the --topic-type parameter along with --location (e.g. "westus2") parameter. For global topic types (e.g. "Microsoft.Resources.Subscriptions"), specify the location value as "global".
    3. To list all event subscriptions in a region (across all topic types), specify only the --location parameter.
    4. For both #2 and #3 above, to filter only by a resource group, you can additionally specify the --resource-group parameter.
parameters:
  - name: --topic-type-name
    short-summary: Name of the topic-type whose event subscriptions need to be listed. When this is specified, you must also specify --location.
    long-summary: |
        Example 1: List all Storage event subscriptions in WestUS2
            --resource-group TestRG --topic-type-name Microsoft.Storage.StorageAccounts --location westus2
        Example 2: List all event subscriptions on Azure subscriptions
            --topic-type-name Microsoft.Resources.Subscriptions --location global
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be listed.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: List all event subscriptions created for an Event Grid topic.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
  - name: List all event subscriptions created for a storage account.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob
  - name: List all event subscriptions created for an Azure subscription.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}
  - name: List all event subscriptions created for a resource group.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
  - name: List all event subscriptions for an Event Grid domain.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1
  - name: List all event subscriptions for an Event Grid domain topic.
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1/topics/topic1
  - name: List all Storage event subscriptions (under the currently selected Azure subscription) in westus2.
    text: |
        az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2
  - name: List all Storage event subscriptions (under the given resource group) in westus2.
    text: |
        az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2 --resource-group {RG}
  - name: List all regional or global event subscriptions (under the currently selected Azure subscription).
    text: |
        az eventgrid event-subscription list --location westus2
        az eventgrid event-subscription list --location global
  - name: List all regional or global event subscriptions under a specified resource group.
    text: |
        az eventgrid event-subscription list --location westus2 --resource-group {RG}
        az eventgrid event-subscription list --location global --resource-group {RG}
  - name: List all event subscriptions for an Event Grid domain whose name contains the pattern "XYZ"
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 --odata-query "Contains(name, 'XYZ')"
  - name: List all event subscriptions for an Event Grid domain except the event subscription with name "name1"
    text: |
        az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid event-subscription show'] = """
type: command
short-summary: Get the details of an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be shown.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
examples:
  - name: Show the details of an event subscription for an Event Grid topic.
    text: |
        az eventgrid event-subscription show --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/topic1
  - name: Show the details of an event subscription for an Azure subscription.
    text: |
        az eventgrid event-subscription show --name es2 \\
            --source-resource-id /subscriptions/{SubID}
  - name: Show the details of an event subscription for a resource group.
    text: |
        az eventgrid event-subscription show --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
  - name: Show the details of an event subscription for a storage account.
    text: |
        az eventgrid event-subscription show --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/microsoft.storage/storageaccounts/kalsegblob
"""

helps['eventgrid event-subscription update'] = """
type: command
short-summary: Update an event subscription.
parameters:
  - name: --source-resource-id
    short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be updated.
    long-summary: |
        Usage:                      --source-resource-id Azure-Resource-ID
        For Azure subscription:     --source-resource-id /subscriptions/{SubID}
        For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
        For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
        For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1
        For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
  - name: --endpoint-type
    short-summary: The type of the destination endpoint.
  - name: --delivery-identity-endpoint-type
    short-summary: The type of the destination endpoint with resource identity.
  - name: --advanced-filter
    short-summary: An advanced filter enables filtering of events based on a specific event property.
    long-summary: |
        Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
        StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
        StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
        StringContains:            --advanced-filter subject StringContains Blue Red
        StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
        StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
        NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
        NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
        NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
        NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
        NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
        NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
        BoolEquals:                --advanced-filter data.property3 BoolEquals true
        Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
examples:
  - name: Update an event subscription for an Event Grid topic to specify a new endpoint.
    text: |
        az eventgrid event-subscription update --name es1 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for an Azure subscription to specify a new subject-ends-with filter.
    text: |
        az eventgrid event-subscription update --name es2 \\
            --source-resource-id /subscriptions/{SubID} \\
            --subject-ends-with .jpg
  - name: Update an event subscription for a resource group to specify a new endpoint and a new subject-ends-with filter.
    text: |
        az eventgrid event-subscription update --name es3 \\
            --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
            --subject-ends-with .png \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
  - name: Update an event subscription for a storage account to specify a new list of included event types.
    text: |
        az eventgrid event-subscription update --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob" \\
            --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
  - name: Update an event subscription for a storage account, to include a deadletter destination.
    text: |
        az eventgrid event-subscription update --name es2 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob" \\
            --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/blobcontainer1
  - name: Update an event subscription for a storage account, using advanced filters.
    text: |
        az eventgrid event-subscription update --name es3 \\
            --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
            --endpoint https://contoso.azurewebsites.net/api/f1?code=code
            --advanced-filter data.blobType StringIn BlockBlob
            --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net

"""

helps['eventgrid extension-topic'] = """
type: group
short-summary: Manage Azure Event Grid extension topics.
"""

helps['eventgrid extension-topic show'] = """
type: command
short-summary: Get the details of an extension topic.
examples:
  - name: Show the details of an extension topic.
    text: az eventgrid extension-topic show --scope /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageAccounts/{StorageAccountName}
"""

helps['eventgrid topic'] = """
type: group
short-summary: Manage Azure Event Grid topics.
"""

helps['eventgrid topic create'] = """
type: command
short-summary: Create a topic.
parameters:
  - name: --inbound-ip-rules
    short-summary: List of inbound IP rules.
    long-summary: |
        List of inbound IP rules specifying IP Address in CIDR notation e.g., 10.0.0.0/8 along with corresponding Action to perform based on the match or no match of the IpMask. Possible values include - Allow.
examples:
  - name: Create a new topic.
    text: az eventgrid topic create -g rg1 --name topic1 -l westus2
  - name: Create a new topic with custom input mappings.
    text: az eventgrid topic create -g rg1 --name topic1 -l westus2 --input-schema customeventschema --input-mapping-fields topic=myTopicField eventType=myEventTypeField --input-mapping-default-values subject=DefaultSubject dataVersion=1.0
  - name: Create a new topic that accepts events published in CloudEvents V1.0 schema.
    text: az eventgrid topic create -g rg1 --name topic1 -l westus2 --input-schema cloudeventschemav1_0
  - name: Create a new topic which allows specific inbound ip rules with Basic Sku and system assigned identity
    text: az eventgrid topic create -g rg1 --name topic1 -l westus2 --public-network-access enabled --inbound-ip-rules 10.0.0.0/8 Allow --inbound-ip-rules 10.2.0.0/8 Allow --sku Basic --identity systemassigned
"""

helps['eventgrid topic delete'] = """
type: command
short-summary: Delete a topic.
examples:
  - name: Delete a topic.
    text: az eventgrid topic delete -g rg1 --name topic1
"""

helps['eventgrid topic private-endpoint-connection'] = """
type: group
short-summary: Manage private endpoint connections of a topic.
"""


helps['eventgrid topic private-endpoint-connection delete'] = """
type: command
short-summary: Delete a private endpoint connection for a topic.
examples:
  - name: Delete private endpoint connection for a specific topic.
    text: az eventgrid topic private-endpoint-connection delete -g rg1 --topic-name topic1 -n connectionName1
"""

helps['eventgrid topic private-endpoint-connection show'] = """
type: command
short-summary: Display the properties of a private endpoint connection for a topic.
examples:
  - name: Show a private endpoint connection for a topic.
    text: az eventgrid topic private-endpoint-connection show -g rg1 --topic-name topic1 -n connectionName1
"""

helps['eventgrid topic private-endpoint-connection list'] = """
type: command
short-summary: List the properties of all the private endpoint connections for a topic.
examples:
  - name: List private endpoint connections for a topic.
    text: az eventgrid topic private-endpoint-connection list -g rg1 --topic-name topic1
"""

helps['eventgrid topic private-endpoint-connection approve'] = """
type: command
short-summary: Approve a private endpoint connection request for a topic.
examples:
  - name: Approve a private endpoint connection for a topic.
    text: az eventgrid topic private-endpoint-connection approve -g rg1 --topic-name topic1 -n topic1-PrivateEndpoint.6d90cf76-a022-452c-9994-6dac62a50c99 --description "Sample approval description"
"""

helps['eventgrid topic private-endpoint-connection reject'] = """
type: command
short-summary: Reject a private endpoint connection request for a topic.
examples:
  - name: Reject a private endpoint connection for a topic.
    text: az eventgrid topic private-endpoint-connection reject -g rg1 --topic-name topic1 -n topic1-PrivateEndpoint.6d90cf76-a022-452c-9994-6dac62a50c99 --description "Sample rejection description"
"""

helps['eventgrid topic private-link-resource'] = """
type: group
short-summary: Manage private link resource of a topic.
"""

helps['eventgrid topic private-link-resource show'] = """
type: command
short-summary: Display the properties of a private link resource for a topic.
examples:
  - name: Show a private endpoint connection for a topic.
    text: az eventgrid topic private-link-resource show -g rg1 --topic-name topic1 -n topic
"""

helps['eventgrid topic private-link-resource list'] = """
type: command
short-summary: List the properties of all the private link resources for a topic.
examples:
  - name: Show a private endpoint connection for a topic.
    text: az eventgrid topic private-link-resource list -g rg1 --topic-name topic1
"""

helps['eventgrid topic key'] = """
type: group
short-summary: Manage shared access keys of a topic.
"""

helps['eventgrid topic key list'] = """
type: command
short-summary: List shared access keys of a topic.
examples:
  - name: List shared access keys of a topic (autogenerated)
    text: az eventgrid topic key list --name MyTopic --resource-group MyResourceGroup
    crafted: true
"""

helps['eventgrid topic key regenerate'] = """
type: command
short-summary: Regenerate a shared access key of a topic.
"""

helps['eventgrid topic list'] = """
type: command
short-summary: List available topics.
examples:
  - name: List all topics in the current Azure subscription.
    text: az eventgrid topic list
  - name: List all topics in a resource group.
    text: az eventgrid topic list -g rg1
  - name: List all topics in a resource group whose name contains the pattern "XYZ"
    text: az eventgrid topic list -g rg1 --odata-query "Contains(name, 'XYZ')"
  - name: List all topics in a resource group except the domain with name "name1"
    text: az eventgrid topic list -g rg1 --odata-query "NOT (name eq 'name1')"
"""

helps['eventgrid topic show'] = """
type: command
short-summary: Get the details of a topic.
examples:
  - name: Show the details of a topic.
    text: az eventgrid topic show -g rg1 -n topic1
  - name: Show the details of a topic based on resource ID.
    text: az eventgrid topic show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
"""

helps['eventgrid topic update'] = """
type: command
short-summary: Update a topic.
parameters:
  - name: --inbound-ip-rules
    short-summary: List of inbound IP rules specifying IP Address in CIDR notation e.g., 10.0.0.0/8 along with corresponding Action to perform based on the match or no match of the IpMask. Possible values include - Allow.
    long-summary: List of inbound IP rules specifying IP Address in CIDR notation e.g., 10.0.0.0/8 along with corresponding Action to perform based on the match or no match of the IpMask. Possible values include - Allow.
examples:
  - name: Update the properties of an existing topic with new sku, identity and public network access information.
    text: az eventgrid topic update -g rg1 --name topic1 --sku Premium --identity systemassigned --public-network-access enabled --inbound-ip-rules 10.0.0.0/8 Allow --inbound-ip-rules 10.2.0.0/8 Allow --tags Dept=IT --sku basic
"""

helps['eventgrid topic-type'] = """
type: group
short-summary: Get details for topic types.
"""

helps['eventgrid topic-type list'] = """
type: command
short-summary: List registered topic types.
"""

helps['eventgrid topic-type list-event-types'] = """
type: command
short-summary: List the event types supported by a topic type.
examples:
  - name: List all event types supported by Azure Storage Accounts.
    text: |
        az eventgrid topic-type list-event-types -n Microsoft.Storage.StorageAccounts
"""

helps['eventgrid topic-type show'] = """
type: command
short-summary: Get the details for a topic type.
"""
