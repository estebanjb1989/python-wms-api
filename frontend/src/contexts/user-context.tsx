'use client';

import * as React from 'react';
import type { User } from '@/types/user';
import { authClient } from '@/lib/auth/client';
import { logger } from '@/lib/default-logger';

export interface UserContextValue {
  user: User | null;
  error: string | null;
  isLoading: boolean;
  checkSession?: () => Promise<void>;
}

export const UserContext = React.createContext<UserContextValue | undefined>(undefined);

export interface UserProviderProps {
  children: React.ReactNode;
}

export function UserProvider({ children }: UserProviderProps): React.JSX.Element {
  const [state, setState] = React.useState<{ user: User | null; error: string | null; isLoading: boolean }>({
    user: null,
    error: null,
    isLoading: true,
  });

  const isCheckingSession = React.useRef(false);

  const checkSession = React.useCallback(async (): Promise<void> => {
    if (isCheckingSession.current) return;
    isCheckingSession.current = true;

    try {
      const accessToken = localStorage.getItem('access_token');

      if (!accessToken) {
        // No token, user definitely not logged in
        setState((prev) => ({ ...prev, user: null, error: null, isLoading: false }));
        return;
      }

      // Token exists, call /me to validate
      const { data, error } = await authClient.getUser();
      console.log({ data, error });

      if (error) {
        if (error === 'Unauthorized' || error === 'Failed to fetch user profile') {
          setState((prev) => ({ ...prev, user: null, error: null, isLoading: false }));
        } else {
          logger.error(error);
          setState((prev) => ({ ...prev, user: null, error: 'Something went wrong', isLoading: false }));
        }
        return;
      }

      setState((prev) => ({ ...prev, user: data ?? null, error: null, isLoading: false }));
    } catch (error) {
      logger.error(error);
      setState((prev) => ({ ...prev, user: null, error: 'Something went wrong', isLoading: false }));
    } finally {
      isCheckingSession.current = false;
    }
  }, []);

  React.useEffect(() => {
    checkSession().catch((err) => {
      logger.error(err);
    });
  }, [checkSession]);

  return <UserContext.Provider value={{ ...state, checkSession }}>{children}</UserContext.Provider>;
}

export const UserConsumer = UserContext.Consumer;
