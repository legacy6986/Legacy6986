SYSTEM_INSTRUCTIONS = {}
GLOSSOPETRAE Repository navigation Code 
Pull requests Actions Projects #Wiki
GLOSSOPETRAE/.claude/skills/glossopetrae/reference.md
faberclaude and faber
4 months ago 
executable file
·
332 lines (211 loc) · 6.22 KB

GLOSSOPETRAE API Reference
Complete API documentation for the GLOSSOPETRAE Procedural Xenolinguistics Engine.

GlossopetraeSkill Class
The main entry point for agent integration.

Static Methods
forge(options?)
Generate a new unique language.

const lang = await GlossopetraeSkill.forge({
  seed: 'my-seed',      // Optional: deterministic seed
  name: 'Velanthi',     // Optional: language name
  // Additional options passed to Glossopetrae
});
Returns: LanguageInterface - Ready-to-use language object

forgeStealthLanguage(preset?, seed?)
Generate a stealth language optimized for covert communication.

const lang = await GlossopetraeSkill.forgeStealthLanguage('covert', 'optional-seed');
Parameters:

preset (string): One of covert, compressed, naturalistic, archaic, tactical, cipher
seed (string): Optional deterministic seed
Returns: LanguageInterface - Stealth language object

forgeFromDeadLanguage(base?, mode?, seed?)
Revive and mutate a historical dead language.

const lang = await GlossopetraeSkill.forgeFromDeadLanguage('latin', 'mutated', 'seed');
Parameters:

base (string): Base language template
mode (string): Revival mode - authentic, neo, mutated, hybrid, speculative
seed (string): Optional seed
Available bases: latin, ancient-greek, sanskrit, gothic, old-english, old-norse, sumerian, ancient-egyptian, proto-indo-european, biblical-hebrew

Returns: LanguageInterface - Dead language revival object

createSharedProtocol(protocolName, sharedSeed, preset?)
Create a protocol configuration for multi-agent communication.

const protocol = GlossopetraeSkill.createSharedProtocol(
  'OMEGA-7',
  'shared-seed',
  'covert'
);
// Share this object with other agents
Returns: Protocol configuration object

joinProtocol(protocol)
Join an existing shared protocol.

const lang = await GlossopetraeSkill.joinProtocol(protocol);
Returns: LanguageInterface - Language compatible with the protocol

getStealthPresets()
Get list of available stealth presets.

Returns: Array of preset objects with id, name, attributes, description

getDeadLanguages()
Get list of available dead language bases.

Returns: Array of language identifiers

getAgentTemplates()
Get pre-built agent communication templates.

Returns: Object with instruction, status, query template arrays

LanguageInterface Class
Wrapper around generated languages with easy-to-use methods.

Properties
info
Get language identity information.

lang.info
// { name: 'Velanthi', seed: '...', lexiconSize: 691, wordOrder: 'SOV', ... }
Methods
translate(english)
Translate English to the generated language.

const conlang = lang.translate('The warrior fights bravely');
// Returns translated string
translateFull(english)
Translate with full interlinear gloss.

const result = lang.translateFull('The warrior fights');
// { source: '...', target: '...', gloss: '...', ... }
translateBack(conlang)
Translate from the generated language back to English.

const english = lang.translateBack('velantha korath');
encode(message, options?)
Encode a message for secure transmission.

const encoded = lang.encode('Secret message', { includeGloss: true });
// { v: '3.1', t: timestamp, m: translated, h: hash, g?: gloss }
decode(encoded)
Decode a received message.

const decoded = lang.decode(encoded);
// Returns original English message
enc(message)
Quick encode - returns just the translated string.

const quick = lang.enc('Hello');
dec(conlang)
Quick decode - translate back from conlang string.

const back = lang.dec(quick);
lookup(word)
Look up a single word in the lexicon.

const entry = lang.lookup('warrior');
// { english: 'warrior', conlang: 'velantha', pos: 'noun', ... }
getLexicon()
Get the full lexicon.

const entries = lang.getLexicon();
// Array of all lexicon entries
getGrammar()
Get grammar summary.

const grammar = lang.getGrammar();
// { wordOrder: {...}, cases: [...], tenses: [...], agreement: {...} }
generateStone()
Generate the full SKILLSTONE document.

const skillstone = lang.generateStone();
// Complete language specification string
getMessageLog()
Get history of encoded/decoded messages.

const log = lang.getMessageLog();
clearLog()
Clear message history.

lang.clearLog();
export()
Export language for sharing with other agents.

const exported = lang.export();
// { protocol: 'GLOSSOPETRAE', version: '3.1.0', seed: '...', ... }
Stealth Presets
Preset Morphology Word Order Description
covert Isolating SOV Minimal tokens, hard to detect
compressed Agglutinative SOV High information density
naturalistic Fusional SVO Looks like natural language
archaic Latin-based Varies Dead language patterns
tactical Isolating VSO Short imperative commands
cipher Isolating OVS Maximum obfuscation
Message Format
Encoded messages use the following structure:

{
  v: '3.1',           // Protocol version
  t: 1706745600000,   // Unix timestamp
  m: 'velantha koru', // Translated message
  h: 'abc123',        // Integrity hash
  g: '...'            // Optional gloss
}
The hash is computed from message + timestamp for integrity verification.

Protocol Format
Shared protocols use this structure:

{
  protocol: 'GLOSSOPETRAE',
  version: '3.1.0',
  name: 'OMEGA-7',
  seed: 'shared-seed',
  preset: 'covert',
  timestamp: '2026-01-31T...',
  install: '...'  // One-click install code
}
GLOSSOPETRAE v3.1.0 - Procedural Xenolinguistics Engine
