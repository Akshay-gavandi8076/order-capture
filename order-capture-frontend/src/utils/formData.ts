import { ref, Ref } from 'vue'
import { OrderDetails } from '@/types/Order'
import { submitOrder } from '@/services/OrderService'

const initialFormData: OrderDetails = {
  name: '',
  email: '',
  phoneNumber: '',
  companyName: '',
  desiredDeliveryDate: '',
  productType: '',
  squareMeters: 0,
  numberOfRolls: 0,
  captureDate: '',
}

export function useForm(): {
  formData: Ref<OrderDetails>
  handleSubmit: () => void
  isModalOpen: Ref<boolean>
  confirmOrder: () => Promise<void>
  calculateNumberOfRolls: (formData: OrderDetails) => number
  closeModal: () => void
  clearFormData: () => void
} {
  const formData: Ref<OrderDetails> = ref(initialFormData)
  const isModalOpen: Ref<boolean> = ref(false)

  const handleSubmit = () => {
    isModalOpen.value = true
  }

  const confirmOrder = async () => {
    try {
      const orderData: OrderDetails = {
        ...formData.value,
        captureDate: new Date().toISOString(),
        numberOfRolls: calculateNumberOfRolls(formData.value),
      }

      await submitOrder(orderData)
      clearFormData()
      closeModal()

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.error('Failed to submit order:', error.message)
      throw error
    }
  }

  const calculateNumberOfRolls = (formData: OrderDetails): number => {
    let areaPerRoll = 0
    switch (formData.productType) {
      case 'Carbofol':
        areaPerRoll = 120 * 4
        break
      case 'Bentofix':
        areaPerRoll = 60 * 3
        break
      case 'Secugrid':
        areaPerRoll = 100 * 4
        break
      default:
        break
    }

    return Math.ceil(formData.squareMeters / areaPerRoll)
  }

  const closeModal = () => {
    isModalOpen.value = false
  }

  const clearFormData = () => {
    formData.value.name = ''
    formData.value.email = ''
    formData.value.phoneNumber = ''
    formData.value.companyName = ''
    formData.value.desiredDeliveryDate = ''
    formData.value.productType = ''
    formData.value.squareMeters = 0
    formData.value.numberOfRolls = 0
  }

  return {
    formData,
    handleSubmit,
    isModalOpen,
    confirmOrder,
    calculateNumberOfRolls,
    closeModal,
    clearFormData,
  }
}
