# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types.projects.contacts import (
    ProfileStatusResponse,
    ProfileExtractResponse,
    ProfileCompressResponse,
    ProfileRetrieveResponse,
    ProfileExtractSyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.retrieve(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.retrieve(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compress(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.compress(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileCompressResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compress(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.compress(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCompressResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compress(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.compress(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCompressResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_compress(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.compress(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.compress(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.export(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.export(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.export(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(object, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_export(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.export(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.export(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.extract(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.extract(
            contact_id="contact_id",
            project_id="project_id",
            force=True,
        )
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.extract(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.extract(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileExtractResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_extract(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.extract(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.extract(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_sync(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_sync_with_all_params(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
            force=True,
        )
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_sync(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_sync(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_extract_sync(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.extract_sync(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.extract_sync(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: DeepRaven) -> None:
        profile = client.projects.contacts.profiles.status(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileStatusResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: DeepRaven) -> None:
        response = client.projects.contacts.profiles.with_raw_response.status(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileStatusResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: DeepRaven) -> None:
        with client.projects.contacts.profiles.with_streaming_response.status(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileStatusResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: DeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.status(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.projects.contacts.profiles.with_raw_response.status(
                contact_id="",
                project_id="project_id",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.retrieve(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.retrieve(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.retrieve(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compress(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.compress(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileCompressResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compress(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.compress(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCompressResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compress(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.compress(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCompressResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_compress(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.compress(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.compress(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.export(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.export(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.export(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(object, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.export(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.export(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.extract(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.extract(
            contact_id="contact_id",
            project_id="project_id",
            force=True,
        )
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.extract(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileExtractResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.extract(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileExtractResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_extract(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.extract(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.extract(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_sync(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_sync_with_all_params(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
            force=True,
        )
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_sync(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_sync(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.extract_sync(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileExtractSyncResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_extract_sync(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.extract_sync(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.extract_sync(
                contact_id="",
                project_id="project_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncDeepRaven) -> None:
        profile = await async_client.projects.contacts.profiles.status(
            contact_id="contact_id",
            project_id="project_id",
        )
        assert_matches_type(ProfileStatusResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.projects.contacts.profiles.with_raw_response.status(
            contact_id="contact_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileStatusResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.projects.contacts.profiles.with_streaming_response.status(
            contact_id="contact_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileStatusResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncDeepRaven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.status(
                contact_id="contact_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.projects.contacts.profiles.with_raw_response.status(
                contact_id="",
                project_id="project_id",
            )
