# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types.projects import KeyListResponse, KeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DeepRaven) -> None:
        key = client.projects.keys.create(
            project_id="project_id",
            name="name",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DeepRaven) -> None:
        response = client.projects.keys.with_raw_response.create(
            project_id="project_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DeepRaven) -> None:
        with client.projects.keys.with_streaming_response.create(
            project_id="project_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.keys.with_raw_response.create(
                project_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DeepRaven) -> None:
        key = client.projects.keys.list(
            "project_id",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DeepRaven) -> None:
        response = client.projects.keys.with_raw_response.list(
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DeepRaven) -> None:
        with client.projects.keys.with_streaming_response.list(
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DeepRaven) -> None:
        key = client.projects.keys.delete(
            key_id="key_id",
            project_id="project_id",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DeepRaven) -> None:
        response = client.projects.keys.with_raw_response.delete(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DeepRaven) -> None:
        with client.projects.keys.with_streaming_response.delete(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.keys.with_raw_response.delete(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.projects.keys.with_raw_response.delete(
                key_id="",
                project_id="project_id",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDeepRaven) -> None:
        key = await async_client.projects.keys.create(
            project_id="project_id",
            name="name",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.keys.with_raw_response.create(
            project_id="project_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.keys.with_streaming_response.create(
            project_id="project_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.keys.with_raw_response.create(
                project_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDeepRaven) -> None:
        key = await async_client.projects.keys.list(
            "project_id",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.keys.with_raw_response.list(
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.keys.with_streaming_response.list(
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeepRaven) -> None:
        key = await async_client.projects.keys.delete(
            key_id="key_id",
            project_id="project_id",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.keys.with_raw_response.delete(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.keys.with_streaming_response.delete(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.keys.with_raw_response.delete(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.projects.keys.with_raw_response.delete(
                key_id="",
                project_id="project_id",
            )
