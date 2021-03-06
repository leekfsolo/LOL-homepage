import React from "react";
import { useTranslation } from "react-i18next";
import MainLayout from "../../common/ui/layout/main-layout";

const HomePage = () => {
  const { t } = useTranslation();

  return <MainLayout>{t("Welcome to React")}</MainLayout>;
};

export default HomePage;
