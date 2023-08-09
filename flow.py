from prefect import task, flow


@task
def emit_event(event, resource, payload):
    return emit_event(
        event=f"slack {payload.get('api_app_id')} {event_type}",
        resource={"prefect.resource.id": f"slack.{channel}.{user}.{ts}"},
        payload=payload,
    )

@flow
def message_flow(event, resource, payload):
    emit_event(event, resource, payload)