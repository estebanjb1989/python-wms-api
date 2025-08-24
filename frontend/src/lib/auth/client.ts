'use client';

import type { User } from '@/types/user';
import { fetchWithAuth } from '../fetch-with-auth';

function generateToken(): string {
  const arr = new Uint8Array(12);
  globalThis.crypto.getRandomValues(arr);
  return Array.from(arr, (v) => v.toString(16).padStart(2, '0')).join('');
}

const user = {
  id: 'USR-000',
  avatar: '/assets/avatar.png',
  firstName: 'Sofia',
  lastName: 'Rivers',
  email: 'sofia@devias.io',
} satisfies User;

export interface SignUpParams {
  firstName: string;
  lastName: string;
  email: string;
  password: string;
}

export interface SignInWithOAuthParams {
  provider: 'google' | 'discord';
}

export interface SignInWithPasswordParams {
  email: string;
  password: string;
}

export interface ResetPasswordParams {
  email: string;
}

const BASE_URL = 'http://localhost:5000';


class AuthClient {
  async signUp(_: SignUpParams): Promise<{ error?: string }> {
    // Make API request

    // We do not handle the API, so we'll just generate a token and store it in localStorage.
    const token = generateToken();
    localStorage.setItem('custom-auth-token', token);

    return {};
  }

  async signInWithOAuth(_: SignInWithOAuthParams): Promise<{ error?: string }> {
    return { error: 'Social authentication not implemented' };
  }

  async signInWithPassword(params: SignInWithPasswordParams): Promise<{ error?: string }> {
    const { email, password } = params;

    try {
      const response = await fetch(`${BASE_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: email, password }),
      });

      if (!response.ok) {
        return { error: 'Invalid credentials' };
      }

      const data = await response.json();
      const { access_token, refresh_token } = data;

      // Store tokens
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);

      return {};
    } catch (error) {
      console.error('Login failed:', error);
      return { error: 'Login failed' };
    }
  }

  async resetPassword(_: ResetPasswordParams): Promise<{ error?: string }> {
    return { error: 'Password reset not implemented' };
  }

  async updatePassword(_: ResetPasswordParams): Promise<{ error?: string }> {
    return { error: 'Update reset not implemented' };
  }

  async getUser(): Promise<{ data?: User | null; error?: string }> {
    try {
      const response = await fetchWithAuth(`${BASE_URL}/me`);

      if (!response.ok) {
        return { data: null, error: 'Failed to fetch user profile' };
      }

      const data = await response.json();
      return { data };
    } catch (error) {
      console.error('Failed to fetch user:', error);
      return { data: null, error: 'Failed to fetch user profile' };
    }
  }

  async signOut(): Promise<{ error?: string }> {
    const refresh_token = localStorage.getItem('refresh_token');

    if (!refresh_token) {
      // No refresh token to revoke, just clear local storage
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      return {};
    }

    try {
      const response = await fetch(`${BASE_URL}/logout`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh_token }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        return { error: errorData.error || 'Logout failed' };
      }

      // Clear tokens locally after successful logout
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      return {};
    } catch (error) {
      console.error('Logout failed:', error);
      return { error: 'Logout failed' };
    }
  }


}

export const authClient = new AuthClient();
