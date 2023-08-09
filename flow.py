from prefect import task, flow

def get_atts(payload, atttribute):
    return payload.get("event").get(atttribute)

@task
def emit_event(payload):

    return emit_event(
     
        event=f"slack {payload.get('api_app_id')} {get_atts(payload, 'type')}",
        resource={"prefect.resource.id": f"slack.{get_atts(payload,'channel')}.{get_atts(payload,'user')}.{get_atts(payload, 'ts')}"},
        payload=payload,
    )

@flow
def message_flow(event, resource, payload):
    emit_event(event, resource, payload)