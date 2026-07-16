/**
 * Iconos inline (contenido interno de <svg>, stroke 24x24).
 * Uso: <svg ... set:html={icons[nombre]} />
 */
export const icons: Record<string, string> = {
  shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
  star: '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
  flame:
    '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
  health:
    '<path d="M12 21C12 21 4 13.5 4 8.5C4 5.5 6.5 3 9.5 3C11 3 12 4 12 4C12 4 13 3 14.5 3C17.5 3 20 5.5 20 8.5C20 13.5 12 21 12 21Z"/><path d="M8 12h2l1.5-3 2 5 1.5-2h2"/>',
  car: '<path d="M5 16l1.5-5h11L19 16"/><rect x="4" y="16" width="16" height="4" rx="1"/><circle cx="7.5" cy="20" r="1"/><circle cx="16.5" cy="20" r="1"/>',
  build: '<path d="M3 21h18M6 21V8l6-4 6 4v13"/><path d="M10 21v-4h4v4M10 12h4"/>',
  tool: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
  food: '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2M7 2v20M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>',
  law: '<path d="M12 3v18M3 7h18M6 7l-3 6a3 3 0 0 0 6 0l-3-6zM18 7l-3 6a3 3 0 0 0 6 0l-3-6z"/>',
  tech: '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
  clean: '<path d="M9 3h6l-1 7H10L9 3zM8 10h8l1 11H7l1-11z"/>',
  truck:
    '<rect x="1" y="5" width="14" height="12" rx="1"/><path d="M15 9h4l3 3v5h-7V9z"/><circle cx="6" cy="19" r="1.5"/><circle cx="18" cy="19" r="1.5"/>',
  pet: '<circle cx="6" cy="8" r="2"/><circle cx="12" cy="5" r="2"/><circle cx="18" cy="8" r="2"/><path d="M12 11c-3 0-6 2.5-6 5.5 0 2 1.5 3.5 3.5 3.5h5c2 0 3.5-1.5 3.5-3.5 0-3-3-5.5-6-5.5z"/>',
  beauty: '<path d="M12 2l2 5 5 .7-3.7 3.5.9 5.3L12 14l-4.2 2.5.9-5.3L5 7.7 10 7l2-5z"/>',
  edu: '<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
};
