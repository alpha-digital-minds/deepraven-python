# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deepraven import DeepRaven, AsyncDeepRaven
from tests.utils import assert_matches_type
from deepraven.types import (
    AuthLoginResponse,
    AuthRefreshResponse,
    AuthRegisterResponse,
    AuthVerifyOtpResponse,
    AuthUpdatePasswordResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_login(self, client: DeepRaven) -> None:
        auth = client.auth.login(
            email="email",
            password="password",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_login(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.login(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_login(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.login(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh(self, client: DeepRaven) -> None:
        auth = client.auth.refresh(
            refresh_token="refresh_token",
        )
        assert_matches_type(AuthRefreshResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.refresh(
            refresh_token="refresh_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRefreshResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.refresh(
            refresh_token="refresh_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRefreshResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register(self, client: DeepRaven) -> None:
        auth = client.auth.register(
            email="email",
            password="password",
        )
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: DeepRaven) -> None:
        auth = client.auth.register(
            email="email",
            password="password",
            name="name",
        )
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.register(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.register(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRegisterResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resend_otp(self, client: DeepRaven) -> None:
        auth = client.auth.resend_otp(
            email="email",
        )
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resend_otp(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.resend_otp(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resend_otp(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.resend_otp(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_password(self, client: DeepRaven) -> None:
        auth = client.auth.reset_password(
            email="email",
        )
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_password(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.reset_password(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_password(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.reset_password(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_password(self, client: DeepRaven) -> None:
        auth = client.auth.update_password(
            access_token="access_token",
            password="password",
        )
        assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_password(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.update_password(
            access_token="access_token",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_password(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.update_password(
            access_token="access_token",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_otp(self, client: DeepRaven) -> None:
        auth = client.auth.verify_otp(
            token="token",
            email="email",
        )
        assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_otp(self, client: DeepRaven) -> None:
        response = client.auth.with_raw_response.verify_otp(
            token="token",
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_otp(self, client: DeepRaven) -> None:
        with client.auth.with_streaming_response.verify_otp(
            token="token",
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_login(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.login(
            email="email",
            password="password",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.login(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.login(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.refresh(
            refresh_token="refresh_token",
        )
        assert_matches_type(AuthRefreshResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.refresh(
            refresh_token="refresh_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRefreshResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.refresh(
            refresh_token="refresh_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRefreshResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.register(
            email="email",
            password="password",
        )
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.register(
            email="email",
            password="password",
            name="name",
        )
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.register(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRegisterResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.register(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRegisterResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resend_otp(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.resend_otp(
            email="email",
        )
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resend_otp(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.resend_otp(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resend_otp(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.resend_otp(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_password(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.reset_password(
            email="email",
        )
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_password(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.reset_password(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_password(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.reset_password(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_password(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.update_password(
            access_token="access_token",
            password="password",
        )
        assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_password(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.update_password(
            access_token="access_token",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_password(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.update_password(
            access_token="access_token",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthUpdatePasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_otp(self, async_client: AsyncDeepRaven) -> None:
        auth = await async_client.auth.verify_otp(
            token="token",
            email="email",
        )
        assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_otp(self, async_client: AsyncDeepRaven) -> None:
        response = await async_client.auth.with_raw_response.verify_otp(
            token="token",
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_otp(self, async_client: AsyncDeepRaven) -> None:
        async with async_client.auth.with_streaming_response.verify_otp(
            token="token",
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthVerifyOtpResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
