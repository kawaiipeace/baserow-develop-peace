<template>
  <div class="control__elements">
    <textarea
      ref="input"
      v-model="copy"
      type="text"
      class="input field-long-text"
      :class="{ 'input--error': touched && !valid }"
      :disabled="readOnly"
      @focus="select()"
      @blur="unselect()"
    />
    <div v-show="touched && !valid" class="error">
      {{ error }}
    </div>
  </div>
</template>

<script>
import rowEditField from '@baserow/modules/database/mixins/rowEditField'
import rowEditFieldInput from '@baserow/modules/database/mixins/rowEditFieldInput'

export default {
  mixins: [rowEditField, rowEditFieldInput],
}
</script>
