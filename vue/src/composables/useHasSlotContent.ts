import type { ComputedRef, VNode } from 'vue';
import { Comment, computed, useSlots } from 'vue';

export function useHasSlotContent(slotName = 'default'): ComputedRef<boolean> {
  const slots = useSlots();

  return computed(() => {
    const slot = slots[slotName];
    const nodes = slot?.();
    if (!nodes) return false;

    return nodes.some((n: VNode) => {
      if (n.type === Comment) return false; // Ignores placeholder comments like <!--v-if--> which is rendered for empty lists
      if (typeof n.children === 'string' && n.children.trim() === '') return false;
      return true;
    });
  });
}
