import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardHeader from '@mui/material/CardHeader';
import Divider from '@mui/material/Divider';
import type { SxProps } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { ArrowRightIcon } from '@phosphor-icons/react/dist/ssr/ArrowRight';
import { Typography } from '@mui/material';

type DataItemKey = keyof DataItem;

export interface DataItem {
  id: string;
  image: string;
  name: string;
  updatedAt: Date;
  [key: string]: any;
}

export interface DataTableProps {
  data?: DataItem[];
  sx?: SxProps;
  title?: string;
  subtitle?: string;
}

export function DataTable({
  data = [],
  sx,
  title,
}: DataTableProps): React.JSX.Element {
  const keys = data && Object.keys(data?.[0] || {})

  return (
    <Card sx={sx}>
      <CardHeader title={title} />
      <Divider />
      <Box sx={{ overflowX: 'auto' }}>
        <Table sx={{ minWidth: 800 }}>
          <TableHead>
            <TableRow key="headings">
              {!!keys?.map(name => {
                return (
                  <TableCell key={name}>{name}</TableCell>
                )
              })}

            </TableRow>
          </TableHead>
          <TableBody>
            {data.map((item) => {
              return (
                <TableRow hover key={item.id}>
                  {keys?.map(key => (
                    <TableCell key={key}>{item[key]}</TableCell>
                  ))}
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </Box>
      <Divider />
      <CardActions sx={{ justifyContent: 'flex-end' }}>
        <Button
          color="inherit"
          endIcon={<ArrowRightIcon fontSize="var(--icon-fontSize-md)" />}
          size="small"
          variant="text"
        >
          View all
        </Button>
      </CardActions>
    </Card>
  );
}
