<template>
  <form @submit.prevent="submit">
    <FormElement :error="fieldHasErrors('license')" class="control">
      <label class="control__label">{{
        $t('registerLicenseForm.licenseKey')
      }}</label>
      <div class="control__elements">
        <textarea
          ref="license"
          v-model="values.license"
          :class="{ 'input--error': fieldHasErrors('license') }"
          type="text"
          class="input textarea--modal"
          @blur="$v.values.license.$touch()"
        />
        <div v-if="fieldHasErrors('license')" class="error">
          {{ $t('error.requiredField') }}
        </div>
      </div>
    </FormElement>
    <slot></slot>
  </form>
</template>

<script>
import { required } from 'vuelidate/lib/validators'

import form from '@baserow/modules/core/mixins/form'

export default {
  name: 'RegisterLicenseForm',
  mixins: [form],
  data() {
    return {
      values: {
        license: '',
      },
    }
  },
  validations: {
    values: {
      license: { required },
    },
  },
  mounted() {
    this.$refs.license.focus()
  },
}
</script>
