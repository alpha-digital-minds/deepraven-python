# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types.projects import ContactListResponse, ContactRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DeepRaven) -> None:
        contact = client.projects.contacts.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DeepRaven) -> None:
        response = client.projects.contacts.with_raw_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DeepRaven) -> None:
        with client.projects.contacts.with_streaming_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.with_raw_response.retrieve(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.with_raw_response.retrieve(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DeepRaven) -> None:
        contact = client.projects.contacts.list(
            "project_id",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DeepRaven) -> None:
        response = client.projects.contacts.with_raw_response.list(
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DeepRaven) -> None:
        with client.projects.contacts.with_streaming_response.list(
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.with_raw_response.list(
                "",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDeepRaven) -> None:
        contact = await async_client.projects.contacts.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.with_raw_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.with_streaming_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.with_raw_response.retrieve(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.with_raw_response.retrieve(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDeepRaven) -> None:
        contact = await async_client.projects.contacts.list(
            "project_id",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.with_raw_response.list(
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.with_streaming_response.list(
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.with_raw_response.list(
                "",
            )
