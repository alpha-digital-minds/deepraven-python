# Auth

Types:

```python
from deepraven.types import (
    AuthLoginResponse,
    AuthRefreshResponse,
    AuthRegisterResponse,
    AuthUpdatePasswordResponse,
    AuthVerifyOtpResponse,
)
```

Methods:

- <code title="post /api/v1/auth/login">client.auth.<a href="./src/deepraven/resources/auth.py">login</a>(\*\*<a href="src/deepraven/types/auth_login_params.py">params</a>) -> <a href="./src/deepraven/types/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /api/v1/auth/refresh">client.auth.<a href="./src/deepraven/resources/auth.py">refresh</a>(\*\*<a href="src/deepraven/types/auth_refresh_params.py">params</a>) -> <a href="./src/deepraven/types/auth_refresh_response.py">AuthRefreshResponse</a></code>
- <code title="post /api/v1/auth/register">client.auth.<a href="./src/deepraven/resources/auth.py">register</a>(\*\*<a href="src/deepraven/types/auth_register_params.py">params</a>) -> <a href="./src/deepraven/types/auth_register_response.py">AuthRegisterResponse</a></code>
- <code title="post /api/v1/auth/resend-otp">client.auth.<a href="./src/deepraven/resources/auth.py">resend_otp</a>(\*\*<a href="src/deepraven/types/auth_resend_otp_params.py">params</a>) -> None</code>
- <code title="post /api/v1/auth/reset-password">client.auth.<a href="./src/deepraven/resources/auth.py">reset_password</a>(\*\*<a href="src/deepraven/types/auth_reset_password_params.py">params</a>) -> None</code>
- <code title="post /api/v1/auth/update-password">client.auth.<a href="./src/deepraven/resources/auth.py">update_password</a>(\*\*<a href="src/deepraven/types/auth_update_password_params.py">params</a>) -> <a href="./src/deepraven/types/auth_update_password_response.py">AuthUpdatePasswordResponse</a></code>
- <code title="post /api/v1/auth/verify-otp">client.auth.<a href="./src/deepraven/resources/auth.py">verify_otp</a>(\*\*<a href="src/deepraven/types/auth_verify_otp_params.py">params</a>) -> <a href="./src/deepraven/types/auth_verify_otp_response.py">AuthVerifyOtpResponse</a></code>

# Projects

Types:

```python
from deepraven.types import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectUpdateResponse,
    ProjectListResponse,
)
```

Methods:

- <code title="post /api/v1/projects">client.projects.<a href="./src/deepraven/resources/projects/projects.py">create</a>(\*\*<a href="src/deepraven/types/project_create_params.py">params</a>) -> <a href="./src/deepraven/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /api/v1/projects/{project_id}">client.projects.<a href="./src/deepraven/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/deepraven/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="patch /api/v1/projects/{project_id}">client.projects.<a href="./src/deepraven/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/deepraven/types/project_update_params.py">params</a>) -> <a href="./src/deepraven/types/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="get /api/v1/projects">client.projects.<a href="./src/deepraven/resources/projects/projects.py">list</a>() -> <a href="./src/deepraven/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/v1/projects/{project_id}">client.projects.<a href="./src/deepraven/resources/projects/projects.py">delete</a>(project_id) -> None</code>

## Keys

Types:

```python
from deepraven.types.projects import KeyCreateResponse, KeyListResponse
```

Methods:

- <code title="post /api/v1/projects/{project_id}/keys">client.projects.keys.<a href="./src/deepraven/resources/projects/keys.py">create</a>(project_id, \*\*<a href="src/deepraven/types/projects/key_create_params.py">params</a>) -> <a href="./src/deepraven/types/projects/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /api/v1/projects/{project_id}/keys">client.projects.keys.<a href="./src/deepraven/resources/projects/keys.py">list</a>(project_id) -> <a href="./src/deepraven/types/projects/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /api/v1/projects/{project_id}/keys/{key_id}">client.projects.keys.<a href="./src/deepraven/resources/projects/keys.py">delete</a>(key_id, \*, project_id) -> None</code>

## Contacts

Types:

```python
from deepraven.types.projects import ContactRetrieveResponse, ContactListResponse
```

Methods:

- <code title="get /api/v1/projects/{project_id}/contacts/{contact_id}">client.projects.contacts.<a href="./src/deepraven/resources/projects/contacts/contacts.py">retrieve</a>(contact_id, \*, project_id) -> <a href="./src/deepraven/types/projects/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="get /api/v1/projects/{project_id}/contacts">client.projects.contacts.<a href="./src/deepraven/resources/projects/contacts/contacts.py">list</a>(project_id) -> <a href="./src/deepraven/types/projects/contact_list_response.py">ContactListResponse</a></code>

### Conversations

Types:

```python
from deepraven.types.projects.contacts import ConversationCreateResponse, ConversationListResponse
```

Methods:

- <code title="post /api/v1/projects/{project_id}/contacts/{contact_id}/conversations">client.projects.contacts.conversations.<a href="./src/deepraven/resources/projects/contacts/conversations.py">create</a>(contact_id, \*, project_id, \*\*<a href="src/deepraven/types/projects/contacts/conversation_create_params.py">params</a>) -> <a href="./src/deepraven/types/projects/contacts/conversation_create_response.py">ConversationCreateResponse</a></code>
- <code title="get /api/v1/projects/{project_id}/contacts/{contact_id}/conversations">client.projects.contacts.conversations.<a href="./src/deepraven/resources/projects/contacts/conversations.py">list</a>(contact_id, \*, project_id, \*\*<a href="src/deepraven/types/projects/contacts/conversation_list_params.py">params</a>) -> <a href="./src/deepraven/types/projects/contacts/conversation_list_response.py">ConversationListResponse</a></code>

### Profiles

Types:

```python
from deepraven.types.projects.contacts import (
    ProfileRetrieveResponse,
    ProfileExtractResponse,
    ProfileExtractSyncResponse,
    ProfileStatusResponse,
)
```

Methods:

- <code title="get /api/v1/projects/{project_id}/contacts/{contact_id}/profile">client.projects.contacts.profiles.<a href="./src/deepraven/resources/projects/contacts/profiles.py">retrieve</a>(contact_id, \*, project_id) -> <a href="./src/deepraven/types/projects/contacts/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="delete /api/v1/projects/{project_id}/contacts/{contact_id}/contact">client.projects.contacts.profiles.<a href="./src/deepraven/resources/projects/contacts/profiles.py">delete_contact</a>(contact_id, \*, project_id) -> None</code>
- <code title="post /api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract">client.projects.contacts.profiles.<a href="./src/deepraven/resources/projects/contacts/profiles.py">extract</a>(contact_id, \*, project_id, \*\*<a href="src/deepraven/types/projects/contacts/profile_extract_params.py">params</a>) -> <a href="./src/deepraven/types/projects/contacts/profile_extract_response.py">ProfileExtractResponse</a></code>
- <code title="post /api/v1/projects/{project_id}/contacts/{contact_id}/profile/extract/sync">client.projects.contacts.profiles.<a href="./src/deepraven/resources/projects/contacts/profiles.py">extract_sync</a>(contact_id, \*, project_id, \*\*<a href="src/deepraven/types/projects/contacts/profile_extract_sync_params.py">params</a>) -> <a href="./src/deepraven/types/projects/contacts/profile_extract_sync_response.py">ProfileExtractSyncResponse</a></code>
- <code title="get /api/v1/projects/{project_id}/contacts/{contact_id}/profile/status">client.projects.contacts.profiles.<a href="./src/deepraven/resources/projects/contacts/profiles.py">status</a>(contact_id, \*, project_id) -> <a href="./src/deepraven/types/projects/contacts/profile_status_response.py">ProfileStatusResponse</a></code>
