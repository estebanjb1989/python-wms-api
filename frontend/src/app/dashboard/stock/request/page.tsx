import * as React from 'react';
import type { Metadata } from 'next';
import Stack from '@mui/material/Stack';

import { config } from '@/config';
import { StockList } from '@/components/dashboard/stock/request/stock-list';
import { StockRequestList } from '@/components/dashboard/stock/request/stock-request-list';
import dayjs from 'dayjs';

export const metadata = { title: `Settings | Dashboard | ${config.site.name}` } satisfies Metadata;

export default function Page(): React.JSX.Element {
  return (
    <Stack spacing={3}>
      <StockRequestList />
      <StockList products={[
        {
          id: 'ORD-007',
          customer: { name: 'Ekaterina Tankova' },
          amount: 30.5,
          status: 'pending',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
        {
          id: 'ORD-006',
          customer: { name: 'Cao Yu' },
          amount: 25.1,
          status: 'delivered',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
        {
          id: 'ORD-004',
          customer: { name: 'Alexa Richardson' },
          amount: 10.99,
          status: 'refunded',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
        {
          id: 'ORD-003',
          customer: { name: 'Anje Keizer' },
          amount: 96.43,
          status: 'pending',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
        {
          id: 'ORD-002',
          customer: { name: 'Clarke Gillebert' },
          amount: 32.54,
          status: 'delivered',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
        {
          id: 'ORD-001',
          customer: { name: 'Adam Denisov' },
          amount: 16.76,
          status: 'delivered',
          createdAt: dayjs().subtract(10, 'minutes').toDate(),
        },
      ]} />
    </Stack>
  );
}
