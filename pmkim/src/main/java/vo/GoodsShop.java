package vo;

public class GoodsShop {

    // 상품 판매점 아이디 
    private String goodShopId;

    // 판매점 명 
    private String shopName;

    // 상품 아이디 
    private String goodId;

    public String getGoodShopId() {
        return goodShopId;
    }

    public void setGoodShopId(String goodShopId) {
        this.goodShopId = goodShopId;
    }

    public String getShopName() {
        return shopName;
    }

    public void setShopName(String shopName) {
        this.shopName = shopName;
    }

    public String getGoodId() {
        return goodId;
    }

    public void setGoodId(String goodId) {
        this.goodId = goodId;
    }

    // GoodsShop 모델 복사
    public void CopyData(GoodsShop param)
    {
        this.goodShopId = param.getGoodShopId();
        this.shopName = param.getShopName();
        this.goodId = param.getGoodId();
    }
}
