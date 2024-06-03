import { OrderDetails } from '@/types/Order'
import axios from 'axios'

const API_URL = 'http://localhost:8001'
// const API_URL = 'http://127.0.0.1:8000'

export async function submitOrder(orderData: OrderDetails): Promise<void> {
  try {
    await axios.post(`${API_URL}/order/`, orderData)
  } catch (error) {
    throw new Error('Failed to submit order')
  }
}

// export async function getOrders(): Promise<Order[]> {
//   try {
//     const response = await axios.get(`${API_URL}/orders/`)
//     return response.data
//   } catch (error) {
//     throw new Error('Failed to retrieve orders')
//   }
// }
