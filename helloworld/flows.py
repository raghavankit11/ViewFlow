from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend
from .views import field_response
from .models import HelloWorldProcess, ResponseSubmissionProcess, AUDIT_PASS, AUDIT_FAIL, APPROVE_PASS, APPROVE_FAIL


@frontend.register
class HelloWorldFlow(Flow):
    process_class = HelloWorldProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
            .Then(this.send)
            .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_hello_world_request(self, activation):
        print(activation.process.text)


@frontend.register
class ResponseSubmissionFlow(Flow):
    process_class = ResponseSubmissionProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["response"]
        ).Permission(
            auto_create=True
        ).Next(this.audit)
    )

    audit = (
        flow.View(
            UpdateProcessView,
            fields=["is_audited"]
        ).Permission(
            auto_create=True
        ).Next(this.check_audit)
    )

    check_audit = (
        flow.If(lambda activation:
                activation.process.is_audited == AUDIT_PASS)
            .Then(this.approve)
            .Else(this.end)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["is_approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.is_approved == APPROVE_PASS)
            .Then(this.send)
            .Else(this.end)
    )

    send = (
        flow.Handler(
            this.publish_response
        ).Next(this.end)
    )

    end = flow.End()

    def publish_response(self, activation):
        activation.process.response.is_published = True
        activation.process.response.save()
        print(f'Response {activation.process.response} published')

