'use client';
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';


import { DataTable } from '@/components/core/dataTable';
import { useWarehouses } from '@/store';
import { UpsertInventoryForm } from '@/components/dashboard/inventory/upsert-inventory';


export default function Page(): React.JSX.Element {
  const { warehouses } = useWarehouses()

  return (
    <Stack spacing={3}>
      <div>
        <Typography variant="h4">Inventory</Typography>
      </div>
      <UpsertInventoryForm />
      <DataTable
        data={warehouses}
        title="Inventory"
      />
    </Stack>
  );
}
