# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    auth_login_params,
    auth_refresh_params,
    auth_register_params,
    auth_resend_otp_params,
    auth_verify_otp_params,
    auth_reset_password_params,
    auth_update_password_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_login_response import AuthLoginResponse
from ..types.auth_refresh_response import AuthRefreshResponse
from ..types.auth_register_response import AuthRegisterResponse
from ..types.auth_verify_otp_response import AuthVerifyOtpResponse
from ..types.auth_update_password_response import AuthUpdatePasswordResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alpha-digital-minds/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alpha-digital-minds/deepraven-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def login(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """
        Authenticate with email + password and return a Supabase JWT.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/login",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthLoginResponse,
        )

    def refresh(
        self,
        *,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRefreshResponse:
        """
        Exchange a refresh token for a new access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/refresh",
            body=maybe_transform({"refresh_token": refresh_token}, auth_refresh_params.AuthRefreshParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRefreshResponse,
        )

    def register(
        self,
        *,
        email: str,
        password: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRegisterResponse:
        """Create a new account.

        Supabase sends a confirmation email. If email confirmation
        is disabled in Supabase, a session is returned immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/register",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "name": name,
                },
                auth_register_params.AuthRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRegisterResponse,
        )

    def resend_otp(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resend the signup confirmation OTP to the given email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v1/auth/resend-otp",
            body=maybe_transform({"email": email}, auth_resend_otp_params.AuthResendOtpParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    def reset_password(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Send a password reset email.

        Supabase emails a link that points back to GET
        /auth/confirm?token_hash=...&type=recovery

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v1/auth/reset-password",
            body=maybe_transform({"email": email}, auth_reset_password_params.AuthResetPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    def update_password(
        self,
        *,
        access_token: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthUpdatePasswordResponse:
        """
        Set a new password using the access token obtained from the recovery callback.
        Call this after the user has been redirected to /auth/confirm?type=recovery and
        the dashboard has extracted the access_token from the URL fragment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/update-password",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "password": password,
                },
                auth_update_password_params.AuthUpdatePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthUpdatePasswordResponse,
        )

    def verify_otp(
        self,
        *,
        token: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthVerifyOtpResponse:
        """Verify the 6-digit OTP code sent to the user's email during signup.

        Returns a
        full session on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/verify-otp",
            body=maybe_transform(
                {
                    "token": token,
                    "email": email,
                },
                auth_verify_otp_params.AuthVerifyOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthVerifyOtpResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alpha-digital-minds/deepraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alpha-digital-minds/deepraven-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def login(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """
        Authenticate with email + password and return a Supabase JWT.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/login",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthLoginResponse,
        )

    async def refresh(
        self,
        *,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRefreshResponse:
        """
        Exchange a refresh token for a new access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/refresh",
            body=await async_maybe_transform({"refresh_token": refresh_token}, auth_refresh_params.AuthRefreshParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRefreshResponse,
        )

    async def register(
        self,
        *,
        email: str,
        password: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRegisterResponse:
        """Create a new account.

        Supabase sends a confirmation email. If email confirmation
        is disabled in Supabase, a session is returned immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/register",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "name": name,
                },
                auth_register_params.AuthRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRegisterResponse,
        )

    async def resend_otp(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resend the signup confirmation OTP to the given email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v1/auth/resend-otp",
            body=await async_maybe_transform({"email": email}, auth_resend_otp_params.AuthResendOtpParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    async def reset_password(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Send a password reset email.

        Supabase emails a link that points back to GET
        /auth/confirm?token_hash=...&type=recovery

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v1/auth/reset-password",
            body=await async_maybe_transform({"email": email}, auth_reset_password_params.AuthResetPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    async def update_password(
        self,
        *,
        access_token: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthUpdatePasswordResponse:
        """
        Set a new password using the access token obtained from the recovery callback.
        Call this after the user has been redirected to /auth/confirm?type=recovery and
        the dashboard has extracted the access_token from the URL fragment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/update-password",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "password": password,
                },
                auth_update_password_params.AuthUpdatePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthUpdatePasswordResponse,
        )

    async def verify_otp(
        self,
        *,
        token: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthVerifyOtpResponse:
        """Verify the 6-digit OTP code sent to the user's email during signup.

        Returns a
        full session on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/verify-otp",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "email": email,
                },
                auth_verify_otp_params.AuthVerifyOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthVerifyOtpResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_raw_response_wrapper(
            auth.login,
        )
        self.refresh = to_raw_response_wrapper(
            auth.refresh,
        )
        self.register = to_raw_response_wrapper(
            auth.register,
        )
        self.resend_otp = to_raw_response_wrapper(
            auth.resend_otp,
        )
        self.reset_password = to_raw_response_wrapper(
            auth.reset_password,
        )
        self.update_password = to_raw_response_wrapper(
            auth.update_password,
        )
        self.verify_otp = to_raw_response_wrapper(
            auth.verify_otp,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_raw_response_wrapper(
            auth.login,
        )
        self.refresh = async_to_raw_response_wrapper(
            auth.refresh,
        )
        self.register = async_to_raw_response_wrapper(
            auth.register,
        )
        self.resend_otp = async_to_raw_response_wrapper(
            auth.resend_otp,
        )
        self.reset_password = async_to_raw_response_wrapper(
            auth.reset_password,
        )
        self.update_password = async_to_raw_response_wrapper(
            auth.update_password,
        )
        self.verify_otp = async_to_raw_response_wrapper(
            auth.verify_otp,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_streamed_response_wrapper(
            auth.login,
        )
        self.refresh = to_streamed_response_wrapper(
            auth.refresh,
        )
        self.register = to_streamed_response_wrapper(
            auth.register,
        )
        self.resend_otp = to_streamed_response_wrapper(
            auth.resend_otp,
        )
        self.reset_password = to_streamed_response_wrapper(
            auth.reset_password,
        )
        self.update_password = to_streamed_response_wrapper(
            auth.update_password,
        )
        self.verify_otp = to_streamed_response_wrapper(
            auth.verify_otp,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_streamed_response_wrapper(
            auth.login,
        )
        self.refresh = async_to_streamed_response_wrapper(
            auth.refresh,
        )
        self.register = async_to_streamed_response_wrapper(
            auth.register,
        )
        self.resend_otp = async_to_streamed_response_wrapper(
            auth.resend_otp,
        )
        self.reset_password = async_to_streamed_response_wrapper(
            auth.reset_password,
        )
        self.update_password = async_to_streamed_response_wrapper(
            auth.update_password,
        )
        self.verify_otp = async_to_streamed_response_wrapper(
            auth.verify_otp,
        )
