export function getDistributedHslColor(index: number, total: number): string {
  const fraction = 360 / total + 1;
  const hue = fraction * (index + 1);
  return `hsl(${hue}, 80%, 60%)`;
}
