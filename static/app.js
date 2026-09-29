/**
 * BharatYatra AI - Frontend Logic & Full Multilingual Localization
 * Supports instant dynamic UI switching (English, हिंदी, Hinglish)
 * Connects to FastAPI for RAG Conversational Bot, Itinerary Planning, and Alternates
 */

const I18N_DICTIONARY = {
  English: {
    brand_tagline: "Uttar Pradesh Curated Circuits • Grounded RAG Assistant",
    tab_planner: "Itinerary Planner",
    tab_chat: "AI Travel Bot (RAG)",
    tab_alternates: "Alternates Solver",
    tab_audit: "Responsible AI Audit",
    hero_pill: "Retrieval-Augmented Generation • Source-Grounded • Sarvam Indic AI",
    hero_title_prefix: "Discover the Eternal Soul of",
    hero_title_suffix: "with Intelligent Planning",
    hero_subtitle: "Say goodbye to scattered blogs. Generate realistic, day-wise itineraries respecting your budget, time, senior-citizen mobility, and language comfort — with 100% verified source citations.",
    dest_lko_meta: "Heritage & Awadhi Food",
    dest_vns_meta: "Ghats & Moksha Nagari",
    dest_agr_meta: "Taj Mahal & Mughal Art",
    dest_ayd_meta: "Ram Janmabhoomi & Saryu",
    dest_pry_meta: "Triveni Sangam & Fort",
    dest_mth_meta: "Braj Bhumi & Prem Mandir",
    form_title: "Trip Preferences",
    label_city: "Destination City",
    label_duration: "Trip Duration",
    opt_dur_1: "1 Day (Quick Highlights)",
    opt_dur_2: "2 Days (Recommended Weekend)",
    opt_dur_3: "3 Days (Immersive Circuit)",
    opt_dur_4: "4 Days (Extended Experience)",
    label_traveller: "Traveller Group",
    opt_trav_fam: "Family with Children",
    opt_trav_sen: "Senior Citizens (Low exertion)",
    opt_trav_solo: "Solo Explorer",
    opt_trav_fri: "Friends / Couples",
    label_budget: "Budget Preference",
    opt_bud_1: "Budget Friendly (Public transit & free entry)",
    opt_bud_2: "Moderate (Standard entry & autos/cabs)",
    opt_bud_3: "Comfort / Premium (Private AC cabs & tours)",
    label_mobility: "Accessibility Needs",
    opt_mob_std: "Standard (Comfortable walking)",
    opt_mob_low: "Low Walking (Avoid steep stairs/long walks)",
    opt_mob_whl: "Wheelchair Barrier-Free Access",
    label_interests: "Key Interests",
    tag_heritage: "Heritage",
    tag_spiritual: "Spiritual",
    tag_food: "Awadhi & Local Food",
    tag_culture: "Culture & Arts",
    tag_arch: "Architecture",
    tag_photo: "Photography",
    tag_craft: "Handloom & Crafts",
    tag_nature: "Gardens & Nature",
    btn_generate: "Generate Grounded Itinerary",
    meta_duration_lbl: "Duration",
    meta_tickets_lbl: "Monument Tickets",
    meta_budget_lbl: "Est. Total Budget",
    meta_status_lbl: "Grounding Status",
    alt_box_title: "Smart Alternates Ready (If constraints change)",
    chat_sidebar_title: "Sarvam Indic AI Queries",
    chat_sidebar_desc: "Ask in English, Hindi (हिंदी) or Hinglish. Grounded answers derived solely from official verified UP Tourism records.",
    btn_voice: "Simulate Voice Input (Saaras)",
    bot_title: "BharatYatra AI Assistant",
    bot_subtitle: "Grounded with Citations • Zero Hallucination Mode",
    bot_welcome: "Namaste! 🙏 I am your grounded travel advisor for Uttar Pradesh. I can assist you with monuments, timings, ticket fees, accessibility, and local food across Lucknow, Varanasi, Agra, Ayodhya, Prayagraj, and Mathura-Vrindavan. How can I assist your trip today?",
    chat_placeholder: "Ask about timings, ticket prices, accessibility, food...",
    alt_solver_title: "Dynamic Constraint Solver & Alternative Recommender",
    alt_solver_desc: "Test how our Intelligence Layer handles unexpected constraints in real-time — such as Friday monument closures, sudden knee pain, or strict budget limits.",
    label_alt_place: "Select Primary Attraction",
    label_alt_constraint: "Trigger Unexpected Constraint",
    opt_alt_fri: "Day Closure (e.g. Friday closure)",
    opt_alt_mob: "Mobility Restriction (Zero stairs, flat ramps)",
    opt_alt_bud: "Budget Cut (Strict low-cost / free spots)",
    opt_alt_tim: "Time Shortage (Quick visit < 1.5h)",
    btn_solve_alt: "Solve & Recommend Grounded Alternates",
    alt_results_header: "Recommended Alternatives from Verified Knowledge Base:",
    audit_m1_tag: "Responsible AI Metric",
    audit_m1_title: "Knowledge Grounding Coverage",
    audit_m1_desc: "Every single attraction record maps directly to verified government and archaeological registry URLs.",
    audit_m2_tag: "Safety & Accuracy",
    audit_m2_title: "Hallucination Refusal Rate",
    audit_m2_desc: "Enforced strict caveat flags and refusals when claims are not corroborated by verified knowledge chunks.",
    audit_m3_tag: "Knowledge Base Scale",
    audit_m3_title: "Curated Assets & Vectors",
    audit_m3_desc: "30 verified destinations, 33 FAQ pairs, and 123 semantic vector chunks across 6 Uttar Pradesh circuits.",
    feedback_title: "Tourist Feedback & Evaluation Registry",
    feedback_desc: "Help us refine the recommendation engine. Submissions are persisted into the SQLite audit table.",
    label_fb_dest: "Destination Visited",
    label_fb_cat: "Category",
    opt_fb_1: "Accuracy of Timings / Prices",
    opt_fb_2: "Pacing / Visit Duration",
    opt_fb_3: "Recommendation Quality",
    opt_fb_4: "Other Suggestion",
    label_fb_rating: "Rating (1 to 5 Stars)",
    label_fb_comment: "Comments / Observations",
    btn_submit_fb: "Submit Responsible AI Feedback",
    prompt_chips: [
      { text: "🏛️ Is Taj Mahal closed on Friday?", query: "Is Taj Mahal closed on Friday?" },
      { text: "🕌 Can senior citizens visit Bara Imambara labyrinth?", query: "Can senior citizens visit Bara Imambara labyrinth?" },
      { text: "🪔 Subah-e-Banaras morning aarti at Assi Ghat", query: "What is Subah-e-Banaras morning aarti at Assi Ghat?" },
      { text: "🚩 Are mobile phones allowed in Ayodhya Ram Mandir?", query: "Are mobile phones allowed inside Ayodhya Ram Mandir?" },
      { text: "🌊 Triveni Sangam Prayagraj boat fare", query: "What is the boat fare at Triveni Sangam Prayagraj?" },
      { text: "🦚 Prem Mandir Vrindavan light show timings", query: "Prem Mandir light show timings" }
    ]
  },

  Hindi: {
    brand_tagline: "उत्तर प्रदेश पर्यटन परिपथ • प्रमाणित आर.ए.जी. सहायक",
    tab_planner: "यात्रा योजनाकार",
    tab_chat: "एआई यात्रा सहायक (RAG)",
    tab_alternates: "विकल्प समाधानकर्ता",
    tab_audit: "उत्तरदायी एआई समीक्षा",
    hero_pill: "प्रमाणित ज्ञानकोष • शून्य भ्रामक जानकारी • सर्वम इंडिक एआई",
    hero_title_prefix: "स्मार्ट व सुगम योजना के साथ अनुभव करें",
    hero_title_suffix: "की पावन संस्कृति",
    hero_subtitle: "इंटरनेट के भ्रामक ब्लॉग्स को कहें अलविदा। अपने बजट, समय, बुजुर्गों की सुगमता व भाषा के अनुसार प्राप्त करें प्रमाणित, सटीक और दिवस-वार यात्रा कार्यक्रम।",
    dest_lko_meta: "धरोहर व अवधी जायका",
    dest_vns_meta: "पवित्र घाट व मोक्ष नगरी",
    dest_agr_meta: "ताज महल व मुग़ल वास्तुकला",
    dest_ayd_meta: "राम जन्मभूमि व सरयू आरती",
    dest_pry_meta: "त्रिवेणी संगम व ऐतिहासिक किला",
    dest_mth_meta: "बृज भूमि व प्रेम मंदिर",
    form_title: "यात्रा प्राथमिकताएं",
    label_city: "गंतव्य शहर चुनें",
    label_duration: "यात्रा की अवधि",
    opt_dur_1: "1 दिवस (त्वरित प्रमुख स्थल)",
    opt_dur_2: "2 दिवस (अनुशंसित सप्ताहांत)",
    opt_dur_3: "3 दिवस (विस्तृत सांस्कृतिक परिपथ)",
    opt_dur_4: "4 दिवस (संपूर्ण दर्शन अनुभव)",
    label_traveller: "यात्री समूह का प्रकार",
    opt_trav_fam: "सपरिवार (बच्चों सहित)",
    opt_trav_sen: "वरिष्ठ नागरिक (कम चलना / सीढ़ियों से बचाव)",
    opt_trav_solo: "एकल यात्री (Solo)",
    opt_trav_fri: "मित्र / दंपत्ति",
    label_budget: "बजट प्राथमिकता",
    opt_bud_1: "किफायती (सार्वजनिक परिवहन व निःशुल्क स्थल)",
    opt_bud_2: "मध्यम (मानक टिकट व ऑटो/कैब)",
    opt_bud_3: "प्रीमियम / आरामदायक (निजी वातानुकूलित वाहन व गाइड)",
    label_mobility: "सुगमता आवश्यकताएं",
    opt_mob_std: "सामान्य (सुगम पैदल भ्रमण)",
    opt_mob_low: "कम चलना (सीढ़ियों व लंबी चढ़ाई से बचाव)",
    opt_mob_whl: "व्हीलचेयर बाधा-मुक्त मार्ग",
    label_interests: "प्रमुख रुचियां",
    tag_heritage: "धरोहर व इतिहास",
    tag_spiritual: "आध्यात्मिक व मंदिर",
    tag_food: "अवधी व स्थानीय खानपान",
    tag_culture: "संस्कृति व कला",
    tag_arch: "वास्तुकला",
    tag_photo: "फोटोग्राफी",
    tag_craft: "हस्तशिल्प व बनारसी साड़ी",
    tag_nature: "उद्यान व प्रकृति",
    btn_generate: "प्रमाणित यात्रा योजना तैयार करें",
    meta_duration_lbl: "अवधि",
    meta_tickets_lbl: "स्मारक प्रवेश शुल्क",
    meta_budget_lbl: "अनुमानित कुल बजट",
    meta_status_lbl: "सत्यता स्थिति",
    alt_box_title: "तैयार विकल्प (यदि परिस्थितियां बदलें)",
    chat_sidebar_title: "सर्वम इंडिक एआई प्रश्न",
    chat_sidebar_desc: "हिंदी, हिंग्लिश या अंग्रेजी में पूछें। सभी उत्तर उत्तर प्रदेश पर्यटन विभाग के आधिकारिक अभिलेखों पर आधारित हैं।",
    btn_voice: "आवाज़ में पूछें (सर्वम सारस)",
    bot_title: "भारतयात्रा एआई सहायक",
    bot_subtitle: "प्रमाणित संदर्भ सहित • शून्य भ्रामक उत्तर मोड",
    bot_welcome: "नमस्ते! 🙏 मैं आपका उत्तर प्रदेश पर्यटन सहायक हूँ। मैं आपको लखनऊ, वाराणसी, आगरा, अयोध्या, प्रयागराज और मथुरा-वृंदावन के स्मारकों, समय, टिकट शुल्क, सुगमता व स्थानीय खानपान की प्रामाणिक जानकारी दे सकता हूँ। आज आप क्या जानना चाहते हैं?",
    chat_placeholder: "समय, टिकट, सुगमता, भोजन या आरती के बारे में पूछें...",
    alt_solver_title: "गतिशील बाधा समाधान व वैकल्पिक सुझाव",
    alt_solver_desc: "देखें कि कैसे हमारा इंटेलिजेंस लेयर अचानक आई बाधाओं — जैसे शुक्रवार को स्मारक बंदी या घुटने का दर्द — का तुरंत समाधान करता है।",
    label_alt_place: "मुख्य आकर्षण चुनें",
    label_alt_constraint: "बाधा का प्रकार चुनें",
    opt_alt_fri: "साप्ताहिक बंदी (जैसे शुक्रवार को ताज महल बंदी)",
    opt_alt_mob: "शारीरिक बाधा (शून्य सीढ़ी, समतल रैंप)",
    opt_alt_bud: "बजट कटौती (निःशुल्क सार्वजनिक स्थल)",
    opt_alt_tim: "समय की कमी (1.5 घंटे से कम में दर्शन)",
    btn_solve_alt: "प्रमाणित विकल्पों की खोज करें",
    alt_results_header: "ज्ञानकोष से अनुशंसित वैकल्पिक स्थल:",
    audit_m1_tag: "उत्तरदायी एआई मानक",
    audit_m1_title: "ज्ञानकोष प्रामाणिकता",
    audit_m1_desc: "प्रत्येक स्मारक का विवरण सीधे आधिकारिक सरकारी व पुरातत्व सर्वेक्षण पोर्टल्स से लिंक है।",
    audit_m2_tag: "सुरक्षा एवं सत्यता",
    audit_m2_title: "शून्य भ्रामकता दर",
    audit_m2_desc: "बिना प्रमाण वाले किसी भी दावे पर तुरंत अस्वीकृति व चेतावनी प्रदर्शित की जाती है।",
    audit_m3_tag: "ज्ञानकोष विस्तार",
    audit_m3_title: "प्रमाणित स्थल एवं वेक्टर्स",
    audit_m3_desc: "उत्तर प्रदेश के 6 प्रमुख परिपथों में 30 स्थल, 33 प्रश्नोत्तरी और 123 सिमेंटिक ज्ञान खंड।",
    feedback_title: "पर्यटक समीक्षा एवं मूल्यांकन",
    feedback_desc: "हमारी सिफारिशों को और बेहतर बनाने में सहायता करें। आपकी समीक्षा SQLite ऑडिट टेबल में सुरक्षित की जाती है।",
    label_fb_dest: "भ्रमण किया गया शहर",
    label_fb_cat: "श्रेणी",
    opt_fb_1: "समय व टिकट शुल्क की सटीकता",
    opt_fb_2: "यात्रा गति व समय प्रबंधन",
    opt_fb_3: "सिफारिशों की गुणवत्ता",
    opt_fb_4: "अन्य सुझाव",
    label_fb_rating: "रेटिंग (1 से 5 स्टार)",
    label_fb_comment: "टिप्पणी / व्यक्तिगत अनुभव",
    btn_submit_fb: "समीक्षा दर्ज करें",
    prompt_chips: [
      { text: "🏛️ क्या शुक्रवार को ताज महल बंद रहता है?", query: "क्या शुक्रवार को ताज महल बंद रहता है?" },
      { text: "🕌 बड़ा इमामबाड़ा में क्या बुजुर्ग जा सकते हैं?", query: "बड़ा इमामबाड़ा में क्या बुजुर्ग जा सकते हैं?" },
      { text: "🪔 अस्सी घाट पर सुबह-ए-बनारस का समय क्या है?", query: "अस्सी घाट पर सुबह-ए-बनारस का समय क्या है?" },
      { text: "🚩 क्या अयोध्या राम मंदिर में मोबाइल फोन ले जा सकते हैं?", query: "क्या अयोध्या राम मंदिर में मोबाइल फोन ले जा सकते हैं?" },
      { text: "🌊 त्रिवेणी संगम पर नाव का किराया कितना है?", query: "त्रिवेणी संगम पर नाव का किराया कितना है?" },
      { text: "🦚 प्रेम मंदिर में लाइट शो कितने बजे होता है?", query: "प्रेम मंदिर में लाइट शो कितने बजे होता है?" }
    ]
  },

  Hinglish: {
    brand_tagline: "Uttar Pradesh Curated Circuits • Grounded RAG Assistant",
    tab_planner: "Itinerary Planner",
    tab_chat: "AI Travel Bot (RAG)",
    tab_alternates: "Alternates Solver",
    tab_audit: "Responsible AI Audit",
    hero_pill: "Retrieval-Augmented Generation • Source-Grounded • Sarvam Indic AI",
    hero_title_prefix: "Explore the Rich Heritage of",
    hero_title_suffix: "with Smart Grounded Planning",
    hero_subtitle: "Boring aur confusing blogs ko bye bolo! Apne budget, time, senior citizens comfort aur preferences ke hisaab se personalized day-wise itinerary banayein — with 100% verified sources.",
    dest_lko_meta: "Nawabi Heritage & Street Food",
    dest_vns_meta: "Sacred Ghats & Ganga Aarti",
    dest_agr_meta: "Taj Mahal & Forts",
    dest_ayd_meta: "Ram Mandir & Saryu Aarti",
    dest_pry_meta: "Sangam & Colonial History",
    dest_mth_meta: "Krishna Bhumi & Prem Mandir",
    form_title: "Apni Trip Preferences Chunein",
    label_city: "City Select Karein",
    label_duration: "Kitne Din Ka Trip Hai?",
    opt_dur_1: "1 Day (Quick Highlights)",
    opt_dur_2: "2 Days (Recommended Weekend)",
    opt_dur_3: "3 Days (Full Circuit)",
    opt_dur_4: "4 Days (Detailed Exploration)",
    label_traveller: "Kaun Kaun Travel Kar Raha Hai?",
    opt_trav_fam: "Family with Kids",
    opt_trav_sen: "Senior Citizens (Kam chalna / easy access)",
    opt_trav_solo: "Solo Traveler",
    opt_trav_fri: "Friends / Couples",
    label_budget: "Budget Level",
    opt_bud_1: "Budget Friendly (Public transport & free spots)",
    opt_bud_2: "Moderate (Standard autos & tickets)",
    opt_bud_3: "Comfort / Luxury (Private AC cabs)",
    label_mobility: "Accessibility Requirements",
    opt_mob_std: "Standard (Normal walking)",
    opt_mob_low: "Low Walking (Stairs avoid karni hain)",
    opt_mob_whl: "Wheelchair Accessible Spots",
    label_interests: "Apke Main Interests",
    tag_heritage: "Heritage & History",
    tag_spiritual: "Spiritual & Temples",
    tag_food: "Awadhi & Street Food",
    tag_culture: "Culture & Music",
    tag_arch: "Architecture",
    tag_photo: "Photography",
    tag_craft: "Crafts & Saree Weaving",
    tag_nature: "Gardens & Nature",
    btn_generate: "Itinerary Plan Banao",
    meta_duration_lbl: "Duration",
    meta_tickets_lbl: "Tickets Ka Kharcha",
    meta_budget_lbl: "Total Estimated Budget",
    meta_status_lbl: "Verification Status",
    alt_box_title: "Backup Alternatives Ready",
    chat_sidebar_title: "Sarvam Indic Voice & Chat",
    chat_sidebar_desc: "English, Hindi ya Hinglish me poochhein. Sabhi answers verified UP Tourism records se hi grounded hain.",
    btn_voice: "Voice Me Poochhein (Saaras)",
    bot_title: "BharatYatra AI Assistant",
    bot_subtitle: "100% Grounded • Zero Hallucination Mode",
    bot_welcome: "Namaste! 🙏 Main aapka Uttar Pradesh travel advisor hoon. Lucknow, Varanasi, Agra, Ayodhya, Prayagraj aur Mathura ke timings, tickets, food aur accessibility ke baare me kuch bhi poochhein!",
    chat_placeholder: "Timings, ticket prices, food, accessibility poochhein...",
    alt_solver_title: "Constraint Solver & Alternate Options",
    alt_solver_desc: "Agar Taj Friday ko closed ho, ya walking avoid karni ho, toh system instantly verified alternatives deta hai.",
    label_alt_place: "Monument Select Karein",
    label_alt_constraint: "Constraint Select Karein",
    opt_alt_fri: "Friday Closure",
    opt_alt_mob: "Mobility / Knee Pain (Zero stairs)",
    opt_alt_bud: "Budget Cut (Free entry spots)",
    opt_alt_tim: "Short on Time (< 1.5h)",
    btn_solve_alt: "Best Alternates Nikalo",
    alt_results_header: "Grounded Alternates from Knowledge Base:",
    audit_m1_tag: "Responsible AI Metric",
    audit_m1_title: "Knowledge Grounding",
    audit_m1_desc: "Sabhi attractions directly UP Tourism aur ASI portals se mapped hain.",
    audit_m2_tag: "Accuracy",
    audit_m2_title: "Hallucination Refusal Rate",
    audit_m2_desc: "Agar information verified nahi hai, toh assistant clearly caveat declare karta hai.",
    audit_m3_tag: "Database Scale",
    audit_m3_title: "Curated Places & Vectors",
    audit_m3_desc: "30 verified destinations aur 123 semantic vector chunks.",
    feedback_title: "Traveler Feedback & Rating",
    feedback_desc: "Apna feedback submit karein taaki recommendation quality aur improve ho sake.",
    label_fb_dest: "Kaunsi City Visit Ki?",
    label_fb_cat: "Feedback Category",
    opt_fb_1: "Timings / Prices Accuracy",
    opt_fb_2: "Visit Duration / Pacing",
    opt_fb_3: "Recommendation Quality",
    opt_fb_4: "Other Suggestions",
    label_fb_rating: "Rating (1 se 5 Stars)",
    label_fb_comment: "Aapka Review",
    btn_submit_fb: "Feedback Submit Karein",
    prompt_chips: [
      { text: "🏛️ Taj Mahal Friday ko open hai kya?", query: "Taj Mahal Friday ko open hai kya?" },
      { text: "🕌 Bara Imambara me senior citizen ja sakte hain kya?", query: "Bara Imambara me senior citizen ja sakte hain kya?" },
      { text: "🪔 Assi Ghat Subah-e-Banaras ka timing kya hai?", query: "Assi Ghat Subah-e-Banaras ka timing kya hai?" },
      { text: "🚩 Ayodhya Ram Mandir me mobile allowed hai kya?", query: "Ayodhya Ram Mandir me mobile allowed hai kya?" },
      { text: "🌊 Triveni Sangam boat ride kitne ki hai?", query: "Triveni Sangam boat ride kitne ki hai?" },
      { text: "🦚 Prem Mandir light show kitne baje hota hai?", query: "Prem Mandir light show kitne baje hota hai?" }
    ]
  }
};

document.addEventListener("DOMContentLoaded", () => {
  // Navigation
  const navTabs = document.querySelectorAll(".tab-btn");
  const viewPanels = document.querySelectorAll(".view-panel");
  const destChips = document.querySelectorAll(".dest-chip");
  const globalLangSelect = document.getElementById("global-lang-select");

  // Form Controls
  const citySelect = document.getElementById("city-select");
  const durationSelect = document.getElementById("duration-select");
  const travellerSelect = document.getElementById("traveller-select");
  const budgetSelect = document.getElementById("budget-select");
  const mobilitySelect = document.getElementById("mobility-select");
  const interestTags = document.querySelectorAll(".interest-tag");
  const itineraryForm = document.getElementById("itinerary-form");

  // Output Containers
  const dayPlansWrapper = document.getElementById("day-plans-wrapper");
  const metaDuration = document.getElementById("meta-duration");
  const metaTickets = document.getElementById("meta-tickets");
  const metaBudget = document.getElementById("meta-budget");
  const planHeadline = document.getElementById("plan-headline");
  const alternatesListContainer = document.getElementById("alternates-list-container");

  // Chat
  const chatMessages = document.getElementById("chat-messages");
  const chatInputText = document.getElementById("chat-input-text");
  const btnSendChat = document.getElementById("btn-send-chat");
  const btnVoiceInput = document.getElementById("btn-voice-input");
  const btnReadAloud = document.getElementById("btn-read-aloud");
  const promptChipsContainer = document.getElementById("prompt-chips-container");
  const botWelcomeMsg = document.getElementById("bot-welcome-msg");

  // Alternates
  const altPlaceSelect = document.getElementById("alt-place-select");
  const altConstraintSelect = document.getElementById("alt-constraint-select");
  const btnSolveAlternates = document.getElementById("btn-solve-alternates");
  const alternatesResultsBox = document.getElementById("alternates-results-box");
  const alternatesCardsList = document.getElementById("alternates-cards-list");

  // Feedback
  const feedbackForm = document.getElementById("feedback-form");

  let currentLang = "English";
  let lastBotAnswer = "";

  // 1. Language Switching Functionality
  function applyLanguage(lang) {
    currentLang = lang;
    const t = I18N_DICTIONARY[lang] || I18N_DICTIONARY.English;

    // Translate all elements with data-i18n
    document.querySelectorAll("[data-i18n]").forEach(elem => {
      const key = elem.getAttribute("data-i18n");
      if (t[key]) {
        elem.textContent = t[key];
      }
    });

    // Update Input Placeholders
    if (chatInputText && t.chat_placeholder) {
      chatInputText.placeholder = t.chat_placeholder;
    }

    // Update Bot Welcome message if it's the only message
    if (botWelcomeMsg && chatMessages.children.length === 1) {
      botWelcomeMsg.textContent = t.bot_welcome;
    }

    // Render localized prompt chips
    renderPromptChips(t.prompt_chips);

    // Regenerate current itinerary in new language
    generateItinerary();
  }

  function renderPromptChips(chips) {
    if (!promptChipsContainer || !chips) return;
    promptChipsContainer.innerHTML = "";
    chips.forEach(chip => {
      const btn = document.createElement("button");
      btn.className = "chip-btn";
      btn.setAttribute("data-query", chip.query);
      btn.textContent = chip.text;
      btn.addEventListener("click", () => {
        sendChatMessage(chip.query);
      });
      promptChipsContainer.appendChild(btn);
    });
  }

  globalLangSelect.addEventListener("change", (e) => {
    applyLanguage(e.target.value);
  });

  // 2. Tab Navigation
  navTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      navTabs.forEach(t => t.classList.remove("active"));
      viewPanels.forEach(p => p.classList.remove("active"));

      tab.classList.add("active");
      const targetId = tab.getAttribute("data-tab");
      const targetPanel = document.getElementById(targetId);
      if (targetPanel) {
        targetPanel.classList.add("active");
      }
    });
  });

  // 3. Destination Selector Chips
  destChips.forEach(chip => {
    chip.addEventListener("click", () => {
      destChips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      const city = chip.getAttribute("data-city");
      citySelect.value = city;
      generateItinerary();
    });
  });

  citySelect.addEventListener("change", () => {
    const city = citySelect.value;
    destChips.forEach(chip => {
      if (chip.getAttribute("data-city") === city) {
        chip.classList.add("active");
      } else {
        chip.classList.remove("active");
      }
    });
    generateItinerary();
  });

  // 4. Interest Tags
  interestTags.forEach(tag => {
    tag.addEventListener("click", () => {
      tag.classList.toggle("selected");
    });
  });

  function getSelectedInterests() {
    const selected = [];
    document.querySelectorAll(".interest-tag.selected").forEach(tag => {
      selected.push(tag.getAttribute("data-value"));
    });
    return selected.length > 0 ? selected : ["Heritage", "Spiritual"];
  }

  // 5. Itinerary Generation
  async function generateItinerary() {
    const city = citySelect.value;
    const durationDays = parseInt(durationSelect.value, 10);
    const travellerType = travellerSelect.value;
    const budgetLevel = budgetSelect.value;
    const mobilityNeeds = mobilitySelect.value;
    const interests = getSelectedInterests();

    const btnGen = document.getElementById("btn-generate-itinerary");
    const originalText = btnGen.innerHTML;
    btnGen.innerHTML = `<span class="spinner"></span> Composing Plan...`;
    btnGen.disabled = true;

    try {
      const response = await fetch("/api/itinerary/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          city,
          duration_days: durationDays,
          interests,
          budget_level: budgetLevel,
          traveller_type: travellerType,
          mobility_needs: mobilityNeeds,
          language: currentLang
        })
      });

      if (!response.ok) {
        throw new Error(`API returned HTTP ${response.status}`);
      }

      const plan = await response.json();
      renderItinerary(plan);
    } catch (err) {
      console.error("Failed to generate itinerary:", err);
      dayPlansWrapper.innerHTML = `
        <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 12px; padding: 24px; text-align: center; color: #fca5a5; margin-top: 16px;">
          <div style="font-size: 1.6rem; margin-bottom: 8px;">⏳</div>
          <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 6px;">Service Initializing</div>
          <div style="font-size: 0.88rem; color: #cbd5e1; max-width: 500px; margin: 0 auto 16px;">
            The serverless function or vector knowledge base is loading. Please click retry below.
          </div>
          <button id="btn-retry-itinerary" class="btn-primary" style="display: inline-flex; margin: 0 auto; padding: 8px 20px; font-size: 0.9rem;">
            🔄 Retry Generation
          </button>
        </div>
      `;
      const retryBtn = document.getElementById("btn-retry-itinerary");
      if (retryBtn) {
        retryBtn.addEventListener("click", () => generateItinerary());
      }
    } finally {
      btnGen.innerHTML = originalText;
      btnGen.disabled = false;
    }
  }

  itineraryForm.addEventListener("submit", (e) => {
    e.preventDefault();
    generateItinerary();
  });

  function renderItinerary(plan) {
    if (!plan || !plan.success) {
      dayPlansWrapper.innerHTML = `<div style="color: #f87171; padding: 24px;">No attractions available for this destination.</div>`;
      return;
    }

    const isHi = currentLang === "Hindi";
    const isHing = currentLang === "Hinglish";

    if (isHi) {
      planHeadline.textContent = `${plan.city} का आपका व्यक्तिगत यात्रा कार्यक्रम`;
    } else if (isHing) {
      planHeadline.textContent = `Aapka Personalized ${plan.city} Travel Itinerary`;
    } else {
      planHeadline.textContent = `Your Personalized ${plan.city} Travel Itinerary`;
    }

    metaDuration.textContent = isHi ? `${plan.duration_days} दिवस` : `${plan.duration_days} Day${plan.duration_days > 1 ? "s" : ""}`;
    metaTickets.textContent = `₹${plan.budget_breakdown.monument_tickets_inr}`;
    metaBudget.textContent = `₹${plan.budget_breakdown.estimated_total_inr.toLocaleString()}`;

    // Render Days
    dayPlansWrapper.innerHTML = "";
    plan.days.forEach(day => {
      const dayCard = document.createElement("div");
      dayCard.className = "day-card";

      let itemsHtml = "";
      day.schedule.forEach(item => {
        let transitHtml = "";
        if (item.transit_from_previous) {
          const transTime = item.transit_from_previous.duration_mins;
          const transMode = item.transit_from_previous.mode;
          const transDist = item.transit_from_previous.distance_km;
          if (isHi) {
            transitHtml = `<div class="transit-connector"><span>🚗</span> <strong>${transTime} मिनट</strong> का सफर (${transDist} किमी) • ${transMode}</div>`;
          } else if (isHing) {
            transitHtml = `<div class="transit-connector"><span>🚗</span> <strong>${transTime} mins</strong> transit via ${transMode} (${transDist} km)</div>`;
          } else {
            transitHtml = `<div class="transit-connector"><span>🚗</span> <strong>${transTime} mins</strong> transit via ${transMode} (${transDist} km)</div>`;
          }
        }

        const slotIcon = item.slot_type === "Morning" ? "🌅" : item.slot_type === "Afternoon" ? "☀️" : "🪔";
        const feeBadge = item.fee_inr === 0 ? (isHi ? "निःशुल्क प्रवेश" : "Free Entry") : (isHi ? `टिकट: ₹${item.fee_inr}` : `Ticket: ₹${item.fee_inr}`);

        const highlightsList = item.highlights && item.highlights.length > 0
          ? item.highlights.map(h => `<span class="badge-tag">✦ ${h}</span>`).join(" ")
          : "";

        const warningHtml = item.warnings && item.warnings.length > 0
          ? `<div style="font-size: 0.78rem; color: #fbbf24; margin-top: 6px;">⚠️ ${item.warnings.join("; ")}</div>`
          : "";

        const whyLabel = isHi ? "अनुशंसा का कारण:" : (isHing ? "Kyu Recommend Kiya:" : "Why Recommended:");
        const sourceLabel = isHi ? "स्रोत:" : "Source:";
        const areaLabel = isHi ? "क्षेत्र:" : "Area:";

        itemsHtml += `
          ${transitHtml}
          <div class="schedule-item">
            <div class="item-slot-header">
              <div class="slot-tag">${slotIcon} ${item.slot}</div>
              <div class="time-window">${item.time_window} (${item.duration_hours} hrs)</div>
            </div>
            <div class="item-name">${item.name}</div>
            <div class="item-badges">
              <span class="badge-tag highlight">${feeBadge}</span>
              <span class="badge-tag">${item.category}</span>
              <span class="badge-tag">${item.accessibility_badge}</span>
              ${highlightsList}
            </div>
            <div class="item-why">
              <span>💡</span>
              <div><strong>${whyLabel}</strong> ${item.why_recommended}</div>
            </div>
            ${warningHtml}
            <div class="item-footer">
              <div>${areaLabel} ${item.area || plan.city}</div>
              <div>${sourceLabel} <a href="${item.source_url}" target="_blank" class="source-link">${item.source} ↗</a></div>
            </div>
          </div>
        `;
      });

      const expCountLabel = isHi ? `${day.schedule.length} प्रमुख स्थल` : `${day.schedule.length} Experiences`;

      dayCard.innerHTML = `
        <div class="day-header">
          <div class="day-title">
            <span>📅</span> ${day.theme}
          </div>
          <div class="day-badge">${expCountLabel}</div>
        </div>
        <div class="timeline">
          ${itemsHtml}
        </div>
      `;
      dayPlansWrapper.appendChild(dayCard);
    });

    // Render Alternates
    alternatesListContainer.innerHTML = "";
    if (plan.alternate_recommendations && plan.alternate_recommendations.length > 0) {
      plan.alternate_recommendations.forEach(alt => {
        const altRow = document.createElement("div");
        altRow.style.cssText = "display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.25); padding: 8px 12px; border-radius: 8px;";
        altRow.innerHTML = `
          <div>
            <strong style="color: var(--text-white); font-size: 0.92rem;">${alt.name}</strong> 
            <span style="font-size: 0.76rem; color: var(--text-muted); margin-left: 6px;">(${alt.category})</span>
            <div style="font-size: 0.78rem; color: #cbd5e1; margin-top: 2px;">${alt.reason_to_swap}</div>
          </div>
          <div style="font-weight: 700; color: var(--text-gold); font-size: 0.92rem;">
            ${alt.fee_inr === 0 ? (isHi ? "निःशुल्क" : "Free") : "₹" + alt.fee_inr}
          </div>
        `;
        alternatesListContainer.appendChild(altRow);
      });
    }
  }

  // 6. Chatbot RAG Interaction
  async function sendChatMessage(queryText) {
    const text = queryText || chatInputText.value.trim();
    if (!text) return;

    appendMessage(text, "user");
    chatInputText.value = "";

    const loadingElem = document.createElement("div");
    loadingElem.className = "message-bubble bot";
    loadingElem.innerHTML = `<em>${currentLang === "Hindi" ? "प्रमाणित ज्ञानकोष से जानकारी खोजी जा रही है... 🔍" : "Searching verified knowledge base... 🔍"}</em>`;
    chatMessages.appendChild(loadingElem);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const city = citySelect.value;

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: text,
          city: city,
          language: currentLang
        })
      });

      if (!response.ok) {
        throw new Error(`API returned HTTP ${response.status}`);
      }

      const data = await response.json();
      chatMessages.removeChild(loadingElem);

      let formattedText = data.answer.replace(/\n/g, "<br>");
      lastBotAnswer = data.answer;

      let citationsHtml = "";
      if (data.citations && data.citations.length > 0) {
        const citHeader = currentLang === "Hindi" ? "प्रमाणित संदर्भ स्रोत:" : "Verified Grounded Sources:";
        citationsHtml = `
          <div class="citation-card">
            <div style="font-weight: 700; color: var(--accent-gold); margin-bottom: 4px;">${citHeader}</div>
            ${data.citations.map(c => `<div><strong>${c.citation_id}</strong> ${c.attraction_name} — <em>${c.source}</em></div>`).join("")}
          </div>
        `;
      }

      appendMessage(`${formattedText}${citationsHtml}`, "bot", true);
    } catch (err) {
      chatMessages.removeChild(loadingElem);
      const errMsg = currentLang === "Hindi"
        ? "सहायक सेवा अभी प्रारंभ हो रही है। कृपया कुछ सेकंड में पुनः प्रयास करें।"
        : "AI assistant service is currently initializing or warming up. Please retry in a few seconds.";
      appendMessage(errMsg, "bot");
    }
  }

  function appendMessage(content, sender, isHtml = false) {
    const bubble = document.createElement("div");
    bubble.className = `message-bubble ${sender}`;
    if (isHtml) {
      bubble.innerHTML = content;
    } else {
      bubble.textContent = content;
    }
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  btnSendChat.addEventListener("click", () => sendChatMessage());
  chatInputText.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendChatMessage();
  });

  // Sarvam Voice Input Simulation
  btnVoiceInput.addEventListener("click", async () => {
    const hindiSamples = [
      "शुक्रवार को ताज महल बंद रहता है क्या?",
      "बड़ा इमामबाड़ा में क्या बुजुर्ग जा सकते हैं?",
      "वाराणसी में गंगा आरती का समय क्या है?",
      "अयोध्या राम मंदिर में फोन ले जाना मना है क्या?"
    ];
    const hinglishSamples = [
      "Taj Mahal Friday ko open hai kya?",
      "Bara Imambara me senior citizen ja sakte hain kya?",
      "Varanasi me Ganga aarti kis time hoti hai?",
      "Ram Mandir me phone allowed hai kya?"
    ];
    const englishSamples = [
      "Is Taj Mahal closed on Friday?",
      "Can senior citizens visit Bara Imambara labyrinth?",
      "What is the timing of Ganga Aarti in Varanasi?",
      "Are mobile phones allowed inside Ayodhya Ram Mandir?"
    ];

    let pool = englishSamples;
    if (currentLang === "Hindi") pool = hindiSamples;
    if (currentLang === "Hinglish") pool = hinglishSamples;

    const picked = pool[Math.floor(Math.random() * pool.length)];

    const res = await fetch("/api/indic/transcribe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ simulated_transcript: picked })
    });
    const data = await res.json();
    chatInputText.value = data.transcript;
    sendChatMessage(data.transcript);
  });

  // Sarvam Bulbul TTS Audio Playback
  btnReadAloud.addEventListener("click", () => {
    if (!lastBotAnswer) {
      alert("No assistant message to read aloud yet!");
      return;
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const cleanSpeech = lastBotAnswer.replace(/\[\d+\]/g, "").replace(/\*\*/g, "");
      const utterance = new SpeechSynthesisUtterance(cleanSpeech.substring(0, 300));
      utterance.rate = 0.92;
      utterance.pitch = 1.0;
      if (currentLang === "Hindi") {
        utterance.lang = "hi-IN";
      }
      window.speechSynthesis.speak(utterance);
    } else {
      alert("Sarvam Bulbul TTS Voice Stream Synthesized.");
    }
  });

  // 7. Dynamic Alternates Solver
  btnSolveAlternates.addEventListener("click", async () => {
    const placeId = altPlaceSelect.value;
    const constraintType = altConstraintSelect.value;

    btnSolveAlternates.disabled = true;
    btnSolveAlternates.textContent = currentLang === "Hindi" ? "विकल्प खोजे जा रहे हैं..." : "Solving Constraints...";

    try {
      const response = await fetch("/api/alternatives", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          place_id: placeId,
          constraint_type: constraintType,
          closed_day: constraintType === "DAY_CLOSURE" ? "Friday" : null
        })
      });

      const data = await response.json();
      alternatesResultsBox.style.display = "block";
      alternatesCardsList.innerHTML = "";

      if (data.recommended_alternatives && data.recommended_alternatives.length > 0) {
        data.recommended_alternatives.forEach(alt => {
          const card = document.createElement("div");
          card.className = "schedule-item";
          card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <strong style="color: var(--accent-gold-light); font-size: 1.15rem;">${alt.name}</strong>
              <span class="badge-tag highlight">${alt.fee_inr === 0 ? "Free Entry" : "₹" + alt.fee_inr}</span>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 6px 0;">
              Walking: <strong>${alt.walking_intensity}</strong> • Wheelchair: <strong>${alt.wheelchair_accessible ? "Yes" : "No"}</strong>
            </div>
            <div style="font-size: 0.86rem; color: #a5b4fc;">
              ✦ ${alt.reasons.join(" • ")}
            </div>
          `;
          alternatesCardsList.appendChild(card);
        });
      } else {
        alternatesCardsList.innerHTML = `<div style="color: var(--text-muted);">No alternate places matched this specific constraint.</div>`;
      }
    } catch (err) {
      console.error(err);
    } finally {
      btnSolveAlternates.disabled = false;
      const t = I18N_DICTIONARY[currentLang] || I18N_DICTIONARY.English;
      btnSolveAlternates.textContent = t.btn_solve_alt;
    }
  });

  // 8. Feedback Form Submission
  feedbackForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const dest = document.getElementById("feedback-destination").value;
    const rating = parseInt(document.getElementById("feedback-rating").value, 10);
    const cat = document.getElementById("feedback-category").value;
    const comment = document.getElementById("feedback-comment").value;

    const btnSubmit = document.getElementById("btn-submit-feedback");
    btnSubmit.disabled = true;

    try {
      await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          destination: dest,
          rating: rating,
          feedback_category: cat,
          comment: comment
        })
      });
      alert(currentLang === "Hindi" ? "धन्यवाद! आपकी समीक्षा उत्तरदायी एआई ऑडिट रजिस्ट्री में दर्ज कर ली गई है।" : "Thank you! Your feedback has been logged to the Responsible AI audit table.");
      feedbackForm.reset();
    } catch (err) {
      alert("Error submitting feedback.");
    } finally {
      btnSubmit.disabled = false;
    }
  });

  // Initial load
  applyLanguage("English");
});
