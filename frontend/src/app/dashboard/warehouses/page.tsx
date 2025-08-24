'use client';
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';


import { DataTable } from '@/components/core/dataTable';
import { useWarehouses } from '@/store';
import { UpsertWarehouseForm } from '@/components/dashboard/warehouses/upsert-warehouse';

export default function Page(): React.JSX.Element {
  const { warehouses, getWarehouses } = useWarehouses()

  React.useEffect(() => {
    getWarehouses()
  }, [])

  return (
    <Stack spacing={3}>
      <div>
        <Typography variant="h4">Warehouses</Typography>
      </div>
      <UpsertWarehouseForm />
      <DataTable
        data={warehouses}
        title="Warehouses"
      />
    </Stack>
  );
}
