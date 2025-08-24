import { create } from 'zustand'
import { fetchWithAuth } from '@/lib/fetch-with-auth';

const BASE_URL = 'http://localhost:5000'

interface IWarehouse {
  id: number
  name: string
  location: string
}

interface IWarehousesStore {
  warehouses: IWarehouse[]
  getWarehouses: () => Promise<void>
  setWarehouses: (warehouses: IWarehouse[]) => void
}

const useWarehouses = create<IWarehousesStore>((set) => ({
  warehouses: [],
  getWarehouses: async () => {
    const response = await fetchWithAuth(`${BASE_URL}/warehouses`)
    const data = await response.json()
    set({ warehouses: data })
  },
  setWarehouses: (warehouses: IWarehouse[]) => set({ warehouses }),
}))


export {
  useWarehouses
}