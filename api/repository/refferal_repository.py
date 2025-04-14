from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.referrals_model import ReferralsModel
from api.dto.referral_dto import CreateReferralDTO

class ReferralsRepository:
    async def create_referral(self, db:AsyncSession, referrals_data:CreateReferralDTO):
        new_referral= ReferralsModel(
            id_client=referrals_data.id_client,
            referral_phone = referrals_data.refferal_phone,
            is_active = referrals_data.is_active
        )
        
        db.add(new_referral)
        await db.commit()
        await db.refresh(new_referral)
        return new_referral
    
    async def get_referrals(self, db:AsyncSession, client_id:int):
        query = select(ReferralsModel).where(ReferralsModel.id_client == client_id)
        result = await db.execute(query)
        
        return result.scalars().all()