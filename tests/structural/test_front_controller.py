import pytest

from patterns.structural.front_controller import (
    Dispatcher,
    MobileView,
    Request,
    RequestController,
    TabletView,
)


def test_request_mobile_type():
    request = Request("mobile")
    assert request.type == Request.mobile_type


def test_request_tablet_type():
    request = Request("tablet")
    assert request.type == Request.tablet_type


def test_request_unknown_type():
    request = Request("desktop")
    assert request.type is None


def test_request_case_insensitive():
    request = Request("MOBILE")
    assert request.type == Request.mobile_type


def test_mobile_view():
    view = MobileView()
    # Should not raise errors
    view.show_index_page()


def test_tablet_view():
    view = TabletView()
    # Should not raise errors
    view.show_index_page()


def test_dispatcher_initialization():
    dispatcher = Dispatcher()
    assert isinstance(dispatcher.mobile_view, MobileView)
    assert isinstance(dispatcher.tablet_view, TabletView)


def test_dispatcher_mobile_request():
    dispatcher = Dispatcher()
    request = Request("mobile")
    # Should not raise errors
    dispatcher.dispatch(request)


def test_dispatcher_tablet_request():
    dispatcher = Dispatcher()
    request = Request("tablet")
    # Should not raise errors
    dispatcher.dispatch(request)


def test_dispatcher_unknown_request():
    dispatcher = Dispatcher()
    request = Request("desktop")
    # Should not raise errors
    dispatcher.dispatch(request)


def test_request_controller_initialization():
    controller = RequestController()
    assert isinstance(controller.dispatcher, Dispatcher)


def test_request_controller_dispatch_request():
    controller = RequestController()
    request = Request("mobile")
    # Should not raise errors
    controller.dispatch_request(request)


def test_request_controller_invalid_request():
    controller = RequestController()
    # Should not raise errors for invalid request type
    controller.dispatch_request("mobile")  # String instead of Request object

