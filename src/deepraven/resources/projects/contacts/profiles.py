# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.projects.contacts import profile_extract_params, profile_extract_sync_params
from ....types.projects.contacts.profile_status_response import ProfileStatusResponse
from ....types.projects.contacts.profile_extract_response import ProfileExtractResponse
from ....types.projects.contacts.profile_retrieve_response import ProfileRetrieveResponse
from ....types.projects.contacts.profile_extract_sync_response import ProfileExtractSyncResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """Return the current profile for a contact.

        Creates an empty one if new.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def delete_contact(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all data (contact, profile, conversations) for a contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/contact",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    def extract(
        self,
        contact_id: str,
        *,
        project_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileExtractResponse:
        """Trigger LLM profile extraction in the background.

        Returns immediately.

        - **force=false** (default): only processes new unprocessed conversations.
        - **force=true**: reprocesses ALL conversations from scratch, fully overwrites
          the profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._post(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, profile_extract_params.ProfileExtractParams),
                security={},
            ),
            cast_to=ProfileExtractResponse,
        )

    def extract_sync(
        self,
        contact_id: str,
        *,
        project_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileExtractSyncResponse:
        """
        Same as /extract but synchronous — blocks until done and returns the updated
        profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._post(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract/sync",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, profile_extract_sync_params.ProfileExtractSyncParams),
                security={},
            ),
            cast_to=ProfileExtractSyncResponse,
        )

    def status(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileStatusResponse:
        """
        Check whether profile extraction is currently running for this contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/status",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ProfileStatusResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deepraven-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """Return the current profile for a contact.

        Creates an empty one if new.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def delete_contact(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all data (contact, profile, conversations) for a contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/contact",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    async def extract(
        self,
        contact_id: str,
        *,
        project_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileExtractResponse:
        """Trigger LLM profile extraction in the background.

        Returns immediately.

        - **force=false** (default): only processes new unprocessed conversations.
        - **force=true**: reprocesses ALL conversations from scratch, fully overwrites
          the profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._post(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, profile_extract_params.ProfileExtractParams),
                security={},
            ),
            cast_to=ProfileExtractResponse,
        )

    async def extract_sync(
        self,
        contact_id: str,
        *,
        project_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileExtractSyncResponse:
        """
        Same as /extract but synchronous — blocks until done and returns the updated
        profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._post(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract/sync",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force": force}, profile_extract_sync_params.ProfileExtractSyncParams
                ),
                security={},
            ),
            cast_to=ProfileExtractSyncResponse,
        )

    async def status(
        self,
        contact_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileStatusResponse:
        """
        Check whether profile extraction is currently running for this contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template(
                "/api/v1/projects/{project_id}/contacts/{contact_id}/profile/status",
                project_id=project_id,
                contact_id=contact_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ProfileStatusResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = to_raw_response_wrapper(
            profiles.retrieve,
        )
        self.delete_contact = to_raw_response_wrapper(
            profiles.delete_contact,
        )
        self.extract = to_raw_response_wrapper(
            profiles.extract,
        )
        self.extract_sync = to_raw_response_wrapper(
            profiles.extract_sync,
        )
        self.status = to_raw_response_wrapper(
            profiles.status,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = async_to_raw_response_wrapper(
            profiles.retrieve,
        )
        self.delete_contact = async_to_raw_response_wrapper(
            profiles.delete_contact,
        )
        self.extract = async_to_raw_response_wrapper(
            profiles.extract,
        )
        self.extract_sync = async_to_raw_response_wrapper(
            profiles.extract_sync,
        )
        self.status = async_to_raw_response_wrapper(
            profiles.status,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = to_streamed_response_wrapper(
            profiles.retrieve,
        )
        self.delete_contact = to_streamed_response_wrapper(
            profiles.delete_contact,
        )
        self.extract = to_streamed_response_wrapper(
            profiles.extract,
        )
        self.extract_sync = to_streamed_response_wrapper(
            profiles.extract_sync,
        )
        self.status = to_streamed_response_wrapper(
            profiles.status,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = async_to_streamed_response_wrapper(
            profiles.retrieve,
        )
        self.delete_contact = async_to_streamed_response_wrapper(
            profiles.delete_contact,
        )
        self.extract = async_to_streamed_response_wrapper(
            profiles.extract,
        )
        self.extract_sync = async_to_streamed_response_wrapper(
            profiles.extract_sync,
        )
        self.status = async_to_streamed_response_wrapper(
            profiles.status,
        )
