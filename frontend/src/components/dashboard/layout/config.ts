import type { NavItemConfig } from '@/types/nav';
import { paths } from '@/paths';

export const navItems = [
  { key: 'overview', title: 'Overview', href: paths.dashboard.overview, icon: 'chart-pie' },
  // { key: 'customers', title: 'Customers', href: paths.dashboard.customers, icon: 'users' },
  // { key: 'integrations', title: 'Integrations', href: paths.dashboard.integrations, icon: 'plugs-connected' },
  // { key: 'settings', title: 'Settings', href: paths.dashboard.settings, icon: 'gear-six' },
  // { key: 'account', title: 'Account', href: paths.dashboard.account, icon: 'user' },
  // { key: 'stock-approve', title: 'Stock Approve', href: paths.dashboard.stockApprove, icon: 'x-square' },
  // { key: 'stock-request', title: 'Stock Request', href: paths.dashboard.stockRequest, icon: 'x-square' },
  { key: 'warehouses', title: 'Warehouses', href: paths.dashboard.warehouses, icon: 'x-square' },
  // { key: 'inventory', title: 'Inventory', href: paths.dashboard.inventory, icon: 'x-square' },
  // { key: 'error', title: 'Error', href: paths.errors.notFound, icon: 'x-square' },
] satisfies NavItemConfig[];
