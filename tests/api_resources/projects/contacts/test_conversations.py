# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types.projects.contacts import (
    ConversationListResponse,
    ConversationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DeepRaven) -> None:
        conversation = client.projects.contacts.conversations.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DeepRaven) -> None:
        conversation = client.projects.contacts.conversations.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DeepRaven) -> None:
        response = client.projects.contacts.conversations.with_raw_response.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DeepRaven) -> None:
        with client.projects.contacts.conversations.with_streaming_response.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.conversations.with_raw_response.create(
                contact_id="contact_id",
                project_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.conversations.with_raw_response.create(
                contact_id="",
                project_id="project_id",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DeepRaven) -> None:
        conversation = client.projects.contacts.conversations.list(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DeepRaven) -> None:
        conversation = client.projects.contacts.conversations.list(
            contact_id="contact_id",
            project_id="project_id",
            limit=0,
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DeepRaven) -> None:
        response = client.projects.contacts.conversations.with_raw_response.list(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DeepRaven) -> None:
        with client.projects.contacts.conversations.with_streaming_response.list(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.conversations.with_raw_response.list(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.conversations.with_raw_response.list(
                contact_id="",
                project_id="project_id",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDeepRaven) -> None:
        conversation = await async_client.projects.contacts.conversations.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeepRaven) -> None:
        conversation = await async_client.projects.contacts.conversations.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.conversations.with_raw_response.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.conversations.with_streaming_response.create(
            contact_id="contact_id",
            project_id="project_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.conversations.with_raw_response.create(
                contact_id="contact_id",
                project_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.conversations.with_raw_response.create(
                contact_id="",
                project_id="project_id",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDeepRaven) -> None:
        conversation = await async_client.projects.contacts.conversations.list(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDeepRaven) -> None:
        conversation = await async_client.projects.contacts.conversations.list(
            contact_id="contact_id",
            project_id="project_id",
            limit=0,
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.conversations.with_raw_response.list(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.conversations.with_streaming_response.list(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.conversations.with_raw_response.list(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.conversations.with_raw_response.list(
                contact_id="",
                project_id="project_id",
            )
