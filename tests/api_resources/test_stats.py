# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types import StatUsageResponse, StatOverviewResponse, StatConversationsDailyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_conversations_daily(self, client: DeepRaven) -> None:
        stat = client.stats.conversations_daily()
        assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_conversations_daily(self, client: DeepRaven) -> None:
        response = client.stats.with_raw_response.conversations_daily()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_conversations_daily(self, client: DeepRaven) -> None:
        with client.stats.with_streaming_response.conversations_daily() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_overview(self, client: DeepRaven) -> None:
        stat = client.stats.overview()
        assert_matches_type(StatOverviewResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_overview(self, client: DeepRaven) -> None:
        response = client.stats.with_raw_response.overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatOverviewResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_overview(self, client: DeepRaven) -> None:
        with client.stats.with_streaming_response.overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatOverviewResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_usage(self, client: DeepRaven) -> None:
        stat = client.stats.usage()
        assert_matches_type(StatUsageResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_usage(self, client: DeepRaven) -> None:
        response = client.stats.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatUsageResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_usage(self, client: DeepRaven) -> None:
        with client.stats.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatUsageResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_conversations_daily(self, async_client: AsyncDeepRaven) -> None:
        stat = await async_client.stats.conversations_daily()
        assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_conversations_daily(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.stats.with_raw_response.conversations_daily()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_conversations_daily(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.stats.with_streaming_response.conversations_daily() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatConversationsDailyResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_overview(self, async_client: AsyncDeepRaven) -> None:
        stat = await async_client.stats.overview()
        assert_matches_type(StatOverviewResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_overview(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.stats.with_raw_response.overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatOverviewResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_overview(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.stats.with_streaming_response.overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatOverviewResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_usage(self, async_client: AsyncDeepRaven) -> None:
        stat = await async_client.stats.usage()
        assert_matches_type(StatUsageResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.stats.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatUsageResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.stats.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatUsageResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
