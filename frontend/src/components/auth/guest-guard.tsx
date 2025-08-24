'use client';

import * as React from 'react';
import { useRouter } from 'next/navigation';
import Alert from '@mui/material/Alert';

import { paths } from '@/paths';
import { logger } from '@/lib/default-logger';
import { useUser } from '@/hooks/use-user';

export interface GuestGuardProps {
  children: React.ReactNode;
}

export function GuestGuard({ children }: GuestGuardProps): React.JSX.Element | null {
  const router = useRouter();
  const { user, error, isLoading } = useUser();
  const [isChecking, setIsChecking] = React.useState(true);
  const [redirected, setRedirected] = React.useState(false); // new state

  const checkPermissions = React.useCallback(async () => {
    if (isLoading || redirected) {
      return;
    }

    if (error) {
      setIsChecking(false);
      return;
    }

    if (user) {
      setRedirected(true);
      router.replace(paths.dashboard.overview);
      return;
    }

    setIsChecking(false);
  }, [isLoading, error, user, redirected, router]);

  React.useEffect(() => {
    checkPermissions().catch(() => {
      // noop
    });
  }, [checkPermissions]);

  if (isChecking) {
    return null;
  }

  if (error) {
    return <Alert color="error">{error}</Alert>;
  }

  return <>{children}</>;
}
