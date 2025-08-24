export async function fetchWithAuth(
  input: RequestInfo,
  init: RequestInit = {}
): Promise<Response> {
  const token = localStorage.getItem('access_token');

  const headers = {
    ...(init.headers || {}),
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };

  return fetch(input, {
    ...init,
    headers,
  });
}
