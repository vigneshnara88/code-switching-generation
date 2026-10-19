# Worked Malay–English rewrites

All 64 source/candidate pairs below were **authored for this guide**. They are not benchmark quotations, native-speaker judgments or audio-confirmed transcripts. The shared default profile is `sg_conversational`; Malaysian and other profiles require contextual review.

The cited rule explains the intended construction; it does not prove the new sentence is natural. Malay/English evidence fields in the JSONL identify illustrative substrings, not exhaustive language annotation. Use [the checklist](../review_checklist.md) before acceptance.

English, Malay and already mixed inputs are included. The four already mixed examples demonstrate that preserving a suitable source is sometimes the right rewrite.

## ME001 — aspect

- **Input (en):** I haven't submitted the form yet.
- **Mixed candidate:** Saya belum submit borang itu.
- **Why:** Belum preserves not yet; tak nak would introduce refusal.
- **Rules:** R02, R16, R19.

## ME002 — negation

- **Input (en):** I don't want to delete this file.
- **Mixed candidate:** Saya tak nak delete fail ini.
- **Why:** Desire is negated; the action is not merely incomplete.
- **Rules:** R17, R18, R19.

## ME003 — aspect

- **Input (en):** I have never used this software.
- **Mixed candidate:** Saya tak pernah guna this software.
- **Why:** Never is preserved; the English noun phrase remains coherent.
- **Rules:** R16, R19, R05.

## ME004 — aspect

- **Input (en):** I no longer work here.
- **Mixed candidate:** Saya tak lagi work here.
- **Why:** No longer describes cessation, not a future intention.
- **Rules:** R19, R02.

## ME005 — scope

- **Input (en):** Not all the files are ready.
- **Mixed candidate:** Bukan semua fail itu ready.
- **Why:** The negation targets all, not each individual file.
- **Rules:** R18, R19.

## ME006 — instruction

- **Input (en):** Don't delete that file.
- **Mixed candidate:** Jangan delete fail itu.
- **Why:** This is a prohibition, not a statement about the speaker's actions.
- **Rules:** R19, R31.

## ME007 — identity

- **Input (en):** That is not my decision.
- **Mixed candidate:** Itu bukan my decision.
- **Why:** Negation targets a noun phrase; ownership remains first person.
- **Rules:** R09, R18.

## ME008 — contrast

- **Input (en):** I agree with the goal, but not the method.
- **Mixed candidate:** Saya setuju dengan the goal, tapi bukan the method.
- **Why:** The contrast concerns the method, not agreement with the goal.
- **Rules:** R18, R30.

## ME009 — pronouns

- **Input (en):** We, including you, can start now.
- **Mixed candidate:** Kita boleh start sekarang.
- **Why:** Kita retains inclusion of the addressee.
- **Rules:** R14, R17.

## ME010 — pronouns

- **Input (en):** We, excluding you, have already started.
- **Mixed candidate:** Kami dah start.
- **Why:** Kami retains exclusion; dah marks the completed start.
- **Rules:** R14, R16.

## ME011 — pronouns

- **Input (ms):** Dia belum sampai.
- **Mixed candidate:** Dia belum arrive.
- **Why:** Dia is retained so the source's unspecified gender is not guessed.
- **Rules:** R14, R16.

## ME012 — permission

- **Input (en):** You are allowed to use this room.
- **Mixed candidate:** You dibenarkan guna bilik ini.
- **Why:** Explicit permission is retained rather than recast as obligation.
- **Rules:** R13, R17.

## ME013 — obligation

- **Input (en):** You must submit it today.
- **Mixed candidate:** You mesti submit it hari ini.
- **Why:** Mesti retains obligation and hari ini retains the deadline day.
- **Rules:** R17, R20.

## ME014 — advice

- **Input (en):** You should check the address first.
- **Mixed candidate:** You patut check alamat itu dulu.
- **Why:** Advice remains weaker than must; dulu retains the order of actions.
- **Rules:** R17, R28.

## ME015 — uncertainty

- **Input (en):** They might arrive late.
- **Mixed candidate:** Mereka mungkin arrive late.
- **Why:** Mungkin retains uncertainty and mereka retains plurality.
- **Rules:** R17, R02.

## ME016 — request

- **Input (en):** Could you check this file now?
- **Mixed candidate:** Boleh check fail ini sekarang?
- **Why:** An ordinary request keeps question force; fail is a Malay noun here.
- **Rules:** R31, R35.

## ME017 — refusal

- **Input (en):** I don't want to join the meeting.
- **Mixed candidate:** Saya tak nak join the meeting.
- **Why:** Do not change unwillingness to inability with tak boleh.
- **Rules:** R17, R19.

## ME018 — ability

- **Input (en):** I can read this document without help.
- **Mixed candidate:** Saya boleh read this document tanpa bantuan.
- **Why:** The context makes ability salient; without help is retained.
- **Rules:** R17, R05.

## ME019 — noun phrase

- **Input (en):** That new draft is very clear.
- **Mixed candidate:** Draft baru itu sangat clear.
- **Why:** Malay modifier and demonstrative order is used around the inserted noun.
- **Rules:** R07, R08, R32.

## ME020 — possession

- **Input (en):** This is my charger.
- **Mixed candidate:** Ini charger saya.
- **Why:** The owner stays first person without an unnecessary possessive wrapper.
- **Rules:** R09, R13.

## ME021 — number

- **Input (en):** I need three files.
- **Mixed candidate:** Saya perlukan three files.
- **Why:** The English count phrase preserves both number and its English plural.
- **Rules:** R10, R11.

## ME022 — classifier

- **Input (en):** Two reviewers are waiting outside.
- **Mixed candidate:** Dua orang reviewer sedang tunggu di luar.
- **Why:** The human classifier fits the referents; ongoing waiting is retained.
- **Rules:** R10, R16.

## ME023 — reduplication

- **Input (en):** The children want to watch a movie.
- **Mixed candidate:** Kanak-kanak itu nak watch a movie.
- **Why:** The lexicalized Malay word is not reduced to kanak.
- **Rules:** R12, R17.

## ME024 — relative clause

- **Input (en):** Use the form that I sent yesterday.
- **Mixed candidate:** Use borang yang saya hantar semalam.
- **Why:** The relative clause identifies which form and retains yesterday.
- **Rules:** R29, R16.

## ME025 — reported speech

- **Input (en):** They said, 'Don't wait,' but I waited.
- **Mixed candidate:** Mereka kata, 'Don't wait,' tapi saya tunggu.
- **Why:** A quoted instruction stays attributed to them; record quotation switching.
- **Rules:** R30, R36.

## ME026 — condition

- **Input (en):** If the train is late, I'll call you.
- **Mixed candidate:** Kalau tren itu lambat, I'll call you.
- **Why:** An uncertain condition remains if, not a prediction that the train will be late.
- **Rules:** R30, R02.

## ME027 — condition

- **Input (en):** I'll go unless it rains.
- **Mixed candidate:** Saya akan pergi unless it rains.
- **Why:** Retaining the English conditional phrase avoids reversing the exception.
- **Rules:** R30, R05.

## ME028 — concession

- **Input (en):** I'll go even if it rains.
- **Mixed candidate:** Saya akan pergi even if it rains.
- **Why:** Even if is different from unless; the intention survives rain.
- **Rules:** R30, R02.

## ME029 — condition

- **Input (en):** You can enter only if you have a ticket.
- **Mixed candidate:** You boleh masuk only if you ada tiket.
- **Why:** Only if preserves a necessary condition rather than merely one possible condition.
- **Rules:** R17, R30.

## ME030 — time

- **Input (en):** Please send it by Friday.
- **Mixed candidate:** Tolong send it by Friday.
- **Why:** The deadline phrase remains intact; by is not replaced with on.
- **Rules:** R31, R36.

## ME031 — time

- **Input (en):** Please call before Friday.
- **Mixed candidate:** Tolong call sebelum hari Jumaat.
- **Why:** Before is retained as sebelum rather than changing to on Friday.
- **Rules:** R28, R31.

## ME032 — quantity

- **Input (en):** The price increased by RM20, not to RM20.
- **Mixed candidate:** Harga itu naik sebanyak RM20, not to RM20.
- **Why:** The amount of change is kept distinct from the resulting price.
- **Rules:** R02, R36.

## ME033 — beneficiary

- **Input (en):** I bought a book for my younger sibling.
- **Mixed candidate:** Saya membelikan adik saya a book.
- **Why:** The beneficiary and purchased object remain distinct; gender is unspecified.
- **Rules:** R22, R09.

## ME034 — passive

- **Input (en):** I have already filled in the form.
- **Mixed candidate:** The form sudah saya isi.
- **Why:** Object-fronted Malay structure retains the actor and completed action.
- **Rules:** R16, R26.

## ME035 — obligation

- **Input (en):** I have to submit it today.
- **Mixed candidate:** Saya kena submit it hari ini.
- **Why:** Kena expresses obligation in this construction.
- **Rules:** R27, R17.

## ME036 — affected participant

- **Input (en):** I got scammed.
- **Mixed candidate:** Saya kena scam.
- **Why:** Here kena marks an affected participant, not a requirement to scam someone.
- **Rules:** R27, R26.

## ME037 — verb insertion

- **Input (en):** I want to print that form.
- **Mixed candidate:** Saya nak print borang itu.
- **Why:** Malay nak licenses the inserted verb without an invented to.
- **Rules:** R20, R08.

## ME038 — english frame

- **Input (en):** I want to print that form.
- **Mixed candidate:** I want to print borang itu.
- **Why:** The English main clause keeps its own infinitival to.
- **Rules:** R04, R20.

## ME039 — phrasal verb

- **Input (en):** I will follow up tomorrow.
- **Mixed candidate:** Saya akan follow up esok.
- **Why:** The English phrasal verb stays coherent and future time is explicit.
- **Rules:** R05, R16.

## ME040 — demonstrative

- **Input (en):** Please check this meeting schedule.
- **Mixed candidate:** Tolong check jadual mesyuarat ini.
- **Why:** This is retained; no duplicate this plus ini is introduced.
- **Rules:** R08, R31.

## ME041 — degree

- **Input (en):** This room is too noisy for me.
- **Mixed candidate:** Bilik ini too noisy untuk saya.
- **Why:** Too retains excess relative to the speaker, not just high volume.
- **Rules:** R06, R32.

## ME042 — location

- **Input (en):** I am waiting at the office.
- **Mixed candidate:** Saya tengah tunggu at the office.
- **Why:** The location is retained as an English phrase; it does not become near the office.
- **Rules:** R16, R28.

## ME043 — time clause

- **Input (en):** I'll call you after I get home.
- **Mixed candidate:** I'll call you selepas saya sampai rumah.
- **Why:** The temporal relation is explicitly after, not an unrelated ending.
- **Rules:** R30, R05.

## ME044 — continuation

- **Input (en):** They are still checking the figures.
- **Mixed candidate:** Mereka masih checking the figures.
- **Why:** The continuing activity is retained; an English ing-form is not categorically banned.
- **Rules:** R16, R20.

## ME045 — state

- **Input (en):** The door is already open.
- **Mixed candidate:** The door dah terbuka.
- **Why:** An open state does not by itself imply an accidental opening.
- **Rules:** R16, R23.

## ME046 — technology

- **Input (en):** My phone is broken, so please call the office.
- **Mixed candidate:** Telefon saya rosak, so please call the office.
- **Why:** Telefon is a Malay lexical form; the later English clause supplies the switch.
- **Rules:** R30, R35.

## ME047 — money

- **Input (en):** I paid SGD30 yesterday.
- **Mixed candidate:** I paid SGD30 semalam.
- **Why:** Currency and amount remain unchanged; an English clause keeps its past tense.
- **Rules:** R16, R36.

## ME048 — health context

- **Input (en):** My appointment is at nine tomorrow morning.
- **Mixed candidate:** Appointment saya pukul sembilan pagi esok.
- **Why:** The time and tomorrow morning remain explicit; no clinic or diagnosis is invented.
- **Rules:** R09, R36.

## ME049 — education

- **Input (en):** The students have not received the results yet.
- **Mixed candidate:** Pelajar-pelajar itu belum terima the results.
- **Why:** The recipients and not-yet meaning remain intact.
- **Rules:** R12, R16.

## ME050 — travel

- **Input (en):** I'll wait on platform two.
- **Mixed candidate:** Saya akan tunggu on platform two.
- **Why:** The future plan, platform and number stay intact; no station name is invented.
- **Rules:** R16, R28, R36.

## ME051 — family

- **Input (en):** My older sibling will call after work.
- **Mixed candidate:** My older sibling akan call selepas kerja.
- **Why:** Keeping the English kinship phrase preserves age and unspecified gender without inventing abang or kakak.
- **Rules:** R02, R14.

## ME052 — public service

- **Input (en):** Where should I submit this application?
- **Mixed candidate:** Di mana saya patut submit permohonan ini?
- **Why:** A conversational question retains destination and advice; formal writing may use a different question form.
- **Rules:** R17, R31.

## ME053 — request

- **Input (ms):** Tolong semak alamat ini dahulu.
- **Mixed candidate:** Tolong check alamat ini dulu.
- **Why:** This is a meaning-preserving rewrite of Malay input, not a transcript correction.
- **Rules:** R01, R31.

## ME054 — aspect

- **Input (ms):** Saya belum menghantar dokumen itu.
- **Mixed candidate:** Saya belum send dokumen itu.
- **Why:** Switching the verb keeps the incomplete action and document reference.
- **Rules:** R01, R16.

## ME055 — condition

- **Input (ms):** Kalau awak lapang esok, kita boleh berbincang.
- **Mixed candidate:** Kalau you free esok, kita boleh discuss.
- **Why:** The condition, tomorrow and inclusive discussion are retained.
- **Rules:** R14, R17, R30.

## ME056 — possession

- **Input (ms):** Buku itu bukan milik saya.
- **Mixed candidate:** That book bukan milik saya.
- **Why:** The denial concerns ownership; an English noun phrase carries the insertion.
- **Rules:** R09, R18.

## ME057 — number

- **Input (ms):** Kami memerlukan dua orang juruteknik.
- **Mixed candidate:** Kami perlukan dua orang technician.
- **Why:** Exclusive we and the number of human referents are preserved.
- **Rules:** R10, R14.

## ME058 — relative clause

- **Input (ms):** Saya mahu buku yang ada di atas meja.
- **Mixed candidate:** Saya nak the book yang ada di atas meja.
- **Why:** The relative location identifies the book; the source is not about any book.
- **Rules:** R17, R29.

## ME059 — negation

- **Input (ms):** Jangan hantar borang itu lagi.
- **Mixed candidate:** Jangan send borang itu lagi.
- **Why:** Lagi can depend on context; this rewrite retains it instead of choosing yet versus again without evidence.
- **Rules:** R19, R20.

## ME060 — ability

- **Input (ms):** Saya tidak dapat membuka pintu itu.
- **Mixed candidate:** Saya tak dapat open pintu itu.
- **Why:** Inability remains distinct from unwillingness or prohibition.
- **Rules:** R17, R18.

## ME061 — minimal edit

- **Input (mixed):** Saya belum submit the form.
- **Mixed candidate:** Saya belum submit the form.
- **Why:** An already suitable mixed source can be retained; rewriting need not maximize changes.
- **Rules:** R01, R02.

## ME062 — minimal edit

- **Input (mixed):** Please call saya bila you sampai.
- **Mixed candidate:** Please call saya bila you sampai.
- **Why:** Preserve an already mixed request and its arrival condition; do not translate it to satisfy a ratio.
- **Rules:** R01, R30.

## ME063 — particle

- **Input (mixed):** You dah check, kan?
- **Mixed candidate:** You dah check, kan?
- **Why:** Retaining kan preserves the appeal for confirmation rather than a neutral question.
- **Rules:** R16, R33.

## ME064 — morphology

- **Input (mixed):** Borang itu di-check semalam.
- **Mixed candidate:** Borang itu di-check semalam.
- **Why:** The passive prefix and English stem are analyzed separately; no actor is invented.
- **Rules:** R24, R25, R40.
