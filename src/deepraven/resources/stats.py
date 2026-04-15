# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.stat_usage_response import StatUsageResponse
from ..types.stat_overview_response import StatOverviewResponse
from ..types.stat_conversations_daily_response import StatConversationsDailyResponse

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)

    def conversations_daily(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatConversationsDailyResponse:
        """Conversation counts per day for the last 30 days."""
        return self._get(
            "/api/v1/stats/conversations/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatConversationsDailyResponse,
        )

    def overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatOverviewResponse:
        """Account-level counts: projects, contacts, conversations, total LLM tokens."""
        return self._get(
            "/api/v1/stats/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatOverviewResponse,
        )

    def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatUsageResponse:
        """Per-project LLM token usage rollup."""
        return self._get(
            "/api/v1/stats/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatUsageResponse,
        )


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)

    async def conversations_daily(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatConversationsDailyResponse:
        """Conversation counts per day for the last 30 days."""
        return await self._get(
            "/api/v1/stats/conversations/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatConversationsDailyResponse,
        )

    async def overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatOverviewResponse:
        """Account-level counts: projects, contacts, conversations, total LLM tokens."""
        return await self._get(
            "/api/v1/stats/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatOverviewResponse,
        )

    async def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatUsageResponse:
        """Per-project LLM token usage rollup."""
        return await self._get(
            "/api/v1/stats/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=StatUsageResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.conversations_daily = to_raw_response_wrapper(
            stats.conversations_daily,
        )
        self.overview = to_raw_response_wrapper(
            stats.overview,
        )
        self.usage = to_raw_response_wrapper(
            stats.usage,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.conversations_daily = async_to_raw_response_wrapper(
            stats.conversations_daily,
        )
        self.overview = async_to_raw_response_wrapper(
            stats.overview,
        )
        self.usage = async_to_raw_response_wrapper(
            stats.usage,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.conversations_daily = to_streamed_response_wrapper(
            stats.conversations_daily,
        )
        self.overview = to_streamed_response_wrapper(
            stats.overview,
        )
        self.usage = to_streamed_response_wrapper(
            stats.usage,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.conversations_daily = async_to_streamed_response_wrapper(
            stats.conversations_daily,
        )
        self.overview = async_to_streamed_response_wrapper(
            stats.overview,
        )
        self.usage = async_to_streamed_response_wrapper(
            stats.usage,
        )
