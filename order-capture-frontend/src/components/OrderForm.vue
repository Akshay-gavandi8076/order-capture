<template>
  <div class="page-container">
    <div class="container">
      <h2 class="center">Order Form</h2>
      <form
        @submit.prevent="handleSubmit"
        class="order-form"
      >
        <div class="form-group">
          <label for="name">Name:</label>
          <input
            type="text"
            id="name"
            v-model="formData.name"
            required
            placeholder="Enter your name"
          />
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input
            type="email"
            id="email"
            v-model="formData.email"
            required
            placeholder="Enter your email"
          />
        </div>
        <div
          class="form-group"
          :class="{ error: phoneNumberError }"
        >
          <label for="phone">Phone Number:</label>
          <input
            type="tel"
            id="phone"
            v-model="formData.phoneNumber"
            required
            @input="handlePhoneNumberInput"
            placeholder="Enter your phone number"
          />
          <span
            v-if="phoneNumberError"
            class="error-message"
            >Phone number must have 11 digits</span
          >
        </div>
        <div class="form-group">
          <label for="company">Company Name:</label>
          <input
            type="text"
            id="company"
            v-model="formData.companyName"
            required
            placeholder="Enter your company name"
          />
        </div>
        <div class="form-group">
          <label for="delivery-date">Desired Delivery Date:</label>
          <input
            type="date"
            id="delivery-date"
            v-model="formData.desiredDeliveryDate"
            required
            :min="getMinDate()"
            placeholder="Select desired delivery date"
          />
        </div>
        <div class="form-group">
          <label for="product">Product Type:</label>
          <select
            id="product"
            v-model="formData.productType"
            required
            placeholder="Select product type"
          >
            <option
              value=""
              disabled
              selected
            >
              Select product type
            </option>
            <option value="Carbofol">Carbofol</option>
            <option value="Bentofix">Bentofix</option>
            <option value="Secugrid">Secugrid</option>
          </select>
        </div>
        <div class="form-group">
          <label for="square-meters">Square Meters:</label>
          <input
            type="number"
            id="square-meters"
            v-model="formData.squareMeters"
            required
            min="1"
            placeholder="Enter square meters"
          />
        </div>
        <div class="center">
          <button
            type="submit"
            class="submit-button"
          >
            Place Order
          </button>
        </div>
      </form>

      <!-- Order Summary Modal -->
      <OrderSummaryModal
        :isOpen="isModalOpen"
        :formData="formData"
        :calculatedNumberOfRolls="calculateNumberOfRolls(formData)"
        @confirm="onConfirmOrder"
        @close="closeModal"
        @clearForm="clearFormData"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useForm } from '@/utils/formData'
import OrderSummaryModal from '@/components/OrderSummaryModal.vue'

export default defineComponent({
  components: {
    OrderSummaryModal,
  },
  setup() {
    const {
      formData,
      handleSubmit,
      isModalOpen,
      confirmOrder,
      calculateNumberOfRolls,
      closeModal,
      clearFormData,
    } = useForm()

    let phoneNumberTimer: ReturnType<typeof setTimeout> | null = null
    const phoneNumberError = ref(false)

    const getMinDate = () => {
      const today = new Date()
      const tomorrow = new Date(today)
      tomorrow.setDate(tomorrow.getDate() + 1)
      return tomorrow.toISOString().split('T')[0]
    }

    const handlePhoneNumberInput = () => {
      // Clear previous timer
      if (phoneNumberTimer) {
        clearTimeout(phoneNumberTimer)
      }

      // Set timer for 500ms
      phoneNumberTimer = setTimeout(() => {
        // Validate phone number
        const cleanedPhoneNumber = formData.value.phoneNumber.replace(/\D/g, '')
        phoneNumberError.value = cleanedPhoneNumber.length !== 11
      }, 500)

      // Reset error message if phone number is valid
      if (!phoneNumberError.value) {
        phoneNumberError.value = false
      }
    }

    // Handle confirm order
    const onConfirmOrder = async () => {
      try {
        await confirmOrder()
        clearFormData()
        closeModal()

        // eslint-disable-next-line @typescript-eslint/no-explicit-any
      } catch (error: any) {
        console.error('Failed to confirm order:', error.message)
      }
    }

    return {
      formData,
      handleSubmit,
      isModalOpen,
      calculateNumberOfRolls,
      closeModal,
      clearFormData,
      phoneNumberError,
      getMinDate,
      handlePhoneNumberInput,
      onConfirmOrder,
    }
  },
})
</script>

<style scoped>
.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 400px;
}

.order-form {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form {
  width: 100%;
}

.form-group {
  margin: 1rem;
}

label {
  font-weight: bold;
}

input[type='text'],
input[type='email'],
input[type='tel'],
input[type='date'],
input[type='number'],
select {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.3rem;
  margin-bottom: 0.3rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  box-sizing: border-box;
}

button[type='submit'] {
  width: 50%;
  padding: 8px;
  margin-top: 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button[type='submit']:hover {
  background-color: #0056b3;
}

.center {
  text-align: center;
}
.error {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 0.8rem;
}
</style>
