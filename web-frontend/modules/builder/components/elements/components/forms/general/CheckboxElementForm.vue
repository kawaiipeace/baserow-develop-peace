<template>
  <form @submit.prevent @keydown.enter.prevent>
    <ApplicationBuilderFormulaInputGroup
      v-model="values.label"
      :label="$t('checkboxElementForm.labelTitle')"
      :placeholder="$t('generalForm.labelPlaceholder')"
      :data-providers-allowed="dataProvidersAllowed"
    ></ApplicationBuilderFormulaInputGroup>
    <ApplicationBuilderFormulaInputGroup
      v-model="values.default_value"
      :label="$t('checkboxElementForm.valueTitle')"
      :placeholder="$t('generalForm.valuePlaceholder')"
      :data-providers-allowed="dataProvidersAllowed"
    ></ApplicationBuilderFormulaInputGroup>
    <FormElement class="control">
      <label class="control__label">
        {{ $t('checkboxElementForm.requiredTitle') }}
      </label>
      <div class="control__elements">
        <Checkbox v-model="values.required"></Checkbox>
      </div>
    </FormElement>
  </form>
</template>

<script>
import form from '@baserow/modules/core/mixins/form'
import ApplicationBuilderFormulaInputGroup from '@baserow/modules/builder/components/ApplicationBuilderFormulaInputGroup.vue'
import {
  CurrentRecordDataProviderType,
  DataSourceDataProviderType,
  PageParameterDataProviderType,
} from '@baserow/modules/builder/dataProviderTypes'

export default {
  name: 'CheckboxElementForm',
  components: { ApplicationBuilderFormulaInputGroup },
  mixins: [form],
  data() {
    return {
      values: {
        label: '',
        default_value: '',
        required: false,
      },
    }
  },
  computed: {
    dataProvidersAllowed() {
      return [
        CurrentRecordDataProviderType.getType(),
        PageParameterDataProviderType.getType(),
        DataSourceDataProviderType.getType(),
      ]
    },
  },
  methods: {
    emitChange(newValues) {
      if (this.isFormValid()) {
        form.methods.emitChange.bind(this)(newValues)
      }
    },
  },
}
</script>
