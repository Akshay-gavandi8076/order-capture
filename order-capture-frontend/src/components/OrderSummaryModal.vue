<template>
  <div
    v-if="isOpen"
    class="modal-overlay"
  >
    <div class="modal">
      <div class="modal-content">
        <span
          class="close"
          @click="closeModal"
          >&times;</span
        >
        <div class="summary-heading">
          <h2>Order Summary</h2>
        </div>

        <div class="summary-item">
          <strong>Name:</strong> {{ formData?.name }}
        </div>
        <div class="summary-item">
          <strong>Email:</strong> {{ formData?.email }}
        </div>
        <div class="summary-item">
          <strong>Phone Number:</strong> {{ formData?.phoneNumber }}
        </div>
        <div class="summary-item">
          <strong>Company Name:</strong> {{ formData?.companyName }}
        </div>
        <div class="summary-item">
          <strong>Desired Delivery Date:</strong>
          {{ formData?.desiredDeliveryDate }}
        </div>
        <div class="summary-item">
          <strong>Product Type:</strong> {{ formData?.productType }}
        </div>
        <div class="summary-item">
          <strong>Square Meters:</strong> {{ formData?.squareMeters }}
        </div>
        <div class="summary-item">
          <strong>Number of Rolls:</strong> {{ calculatedNumberOfRolls }}
        </div>

        <div class="button-container">
          <button
            @click="confirmOrder"
            class="confirm-button"
          >
            Confirm Order
          </button>

          <button
            @click="closeModal"
            class="close-button"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    isOpen: Boolean,
    formData: Object,
    calculatedNumberOfRolls: Number,
  },
  methods: {
    async confirmOrder() {
      try {
        // Emit event to confirm the order
        await this.$emit('confirm')

        // Show alert message
        window.alert('Your order is placed successfully!')

        // eslint-disable-next-line @typescript-eslint/no-explicit-any
      } catch (error: any) {
        // Show error message
        window.alert(`Failed to confirm order: ${error.message}`)
        throw error // rethrow error
      } finally {
        // Emit event to close the modal
        this.$emit('close')

        // Emit event to clear the form data
        this.$emit('clearForm')
      }
    },
    closeModal() {
      this.$emit('close')
    },
  },
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.848);
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 2;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  border-radius: 10px;
  width: 80%;
  max-width: 400px;
  height: 55%;
  overflow-y: auto;
  position: relative;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  color: #aaa;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
}

.button-container {
  display: flex;
  justify-content: space-evenly;
  margin-top: 20px;
}

.confirm-button,
.close-button {
  color: #fff;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  padding: 10px;
  width: 120px;
  height: 40px;
}

.confirm-button {
  background-color: #4caf50;
}

.confirm-button:hover {
  background-color: #388e3c;
}

.close-button {
  background-color: #f44336;
}

.close-button:hover {
  background-color: #d32f2f;
}

.summary-item {
  font-size: 15px;
  margin-bottom: 10px;
  line-height: 1.5;
  color: #333;
  padding-left: 20px;
  padding-right: 20px;
}

.summary-heading {
  text-align: center;
}

@media only screen and (max-width: 768px) {
  .modal-content {
    width: 90%;
    max-width: none;
  }

  .button-container {
    flex-direction: column;
    align-items: center;
    margin-top: 10px;
  }

  .confirm-button,
  .close-button {
    width: 100%;
    margin-top: 10px;
  }
}
</style>
