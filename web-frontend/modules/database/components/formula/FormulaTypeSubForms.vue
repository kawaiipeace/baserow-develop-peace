<template>
  <div>
    <FieldNumberSubForm
      v-if="formulaType === 'number'"
      :default-values="defaultValues"
      :table="table"
      :view="view"
      :allow-set-number-negative="false"
    >
    </FieldNumberSubForm>
    <FieldDateSubForm
      v-else-if="['date', 'last_modified', 'created_on'].includes(formulaType)"
      :default-values="defaultValues"
      :table="table"
      :view="view"
    >
    </FieldDateSubForm>
    <FieldDurationSubForm
      v-else-if="formulaType === 'duration'"
      :default-values="defaultValues"
      :table="table"
      :view="view"
    >
    </FieldDurationSubForm>
  </div>
</template>
<script>
import FieldNumberSubForm from '@baserow/modules/database/components/field/FieldNumberSubForm'
import FieldDateSubForm from '@baserow/modules/database/components/field/FieldDateSubForm'
import FieldDurationSubForm from '@baserow/modules/database/components/field/FieldDurationSubForm'
import form from '@baserow/modules/core/mixins/form'
import fieldSubForm from '@baserow/modules/database/mixins/fieldSubForm'

export default {
  name: 'FormulaTypeSubForms',
  components: {
    FieldNumberSubForm,
    FieldDateSubForm,
    FieldDurationSubForm,
  },
  mixins: [form, fieldSubForm],
  props: {
    table: {
      required: true,
      type: Object,
    },
    formulaType: {
      required: false,
      type: String,
      default: null,
    },
    defaultValues: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      allowedValues: [],
      values: {},
    }
  },
}
</script>
