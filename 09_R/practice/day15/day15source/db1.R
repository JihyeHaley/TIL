View(iris)
iris
# 방법 1
dbWriteTable(conn,"IRIS",data.frame(SLENTH=iris$Sepal.Length, 
                                    SWIDTH=iris$Sepal.Width, 
                                    PLENTH=iris$Petal.Length, 
                                    PWIDTH=iris$Petal.Width, 
                                    SPECIES=iris$Species))

iris2<-dbGetQuery(conn, "SELECT * FROM IRIS")

dbSendUpdate(conn,"ALTER TABLE IRIS RENAME COLUMN SLENTH TO SLENGTH")

library(ggplot2)

draw1<-ggplot(iris2, aes(x=SLENGTH, y=SWIDTH, color=SPECIES))+geom_point()
ggsave("db1.jpg")
draw2<-ggplot(iris2, aes(x=PLENTH, y=PWIDTH, color=SPECIES))+geom_point()
ggsave("db2.jpg")
